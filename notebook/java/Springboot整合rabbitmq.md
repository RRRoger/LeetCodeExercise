# Springboot整合rabbitmq

参考链接：

-   https://blog.csdn.net/qq_35387940/article/details/100514134
-   https://blog.csdn.net/zidongxiangxi/article/details/100623548

## 使用docker安装rabbitmq(本地调试)

>   暴露端口用途(参考： https://www.jianshu.com/p/4e1391de89e1)
>
>   -   15672: 后台管理界面（仅在启用管理插件的情况下）
>   -   5671,5672: AMQP协议
>   -   15671：管理监听端口
>   -   25672：server间内部通信口
>   -   4369：epmd，RabbitMQ节点和CLI工具使用的对等发现服务
>   -   61613,61614: STOMP协议（仅在启用STOMP插件的情况下）
>   -   1883,8883: MQTT协议（仅在启用了Web STOMP插件的情况下）

```bash
docker run -di --name rabbitmq_server \
    -e RABBITMQ_DEFAULT_USER=admin \
    -e RABBITMQ_DEFAULT_PASS=admin \
    -p 15672:15672 -p 5672:5672 -p 25672:25672 \
    -p 61613:61613 -p 1883:1883 rabbitmq:management
```

## rabbitmq常用指令

>   参考： https://segmentfault.com/a/1190000038393678

### 基本操作

1.   rabbitmqctl list_queues 查看队列
2.   rabbitmqctl delete_queue queue1 删除队列
3.   rabbitmqctl purge_queue queue1 清空队列

#### 用户管理

1.   rabbitmqctl list_users 查看所有用户
2.   rabbitmqctl add_user admin admin 新增用户
3.   rabbitmqctl set_user_tags admin administrator 设置角色

### 插件管理

1.   rabbitmq-plugins enable xxxx  启用插件
2.   rabbitmq-plugins disable xxxx 禁用插件
3.   rabbitmq-plugins list 显示所有插件

## 添加依赖：pom.xml

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-amqp</artifactId>
    <version>2.6.2</version>
</dependency>
```

## 配置rabbitmq

```ini
# rabbitmq config
spring.rabbitmq.host=127.0.0.1
spring.rabbitmq.port=5672
spring.rabbitmq.username=admin
spring.rabbitmq.password=admin
spring.rabbitmq.listener.simple.acknowledge-mode=manual
```

## 生产者配置

>   MQConfig.java

```java
import org.springframework.amqp.core.*;
import org.springframework.amqp.rabbit.annotation.EnableRabbit;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@EnableRabbit
public class MQConfig {

    @Bean
    public DirectExchange defaultExchange() {
        boolean durable = true;
        boolean autoDelete = false;
        return new DirectExchange("default_exchange", durable, autoDelete);
    }

    public Queue newQueue(String queue) {
        boolean durable = true;
        boolean exclusive = false;
        boolean autoDelete = false;
        return new Queue("default_queue", durable, exclusive, autoDelete);
    }

    @Bean
    public Queue queue() {
        return this.newQueue(mqProperties.getQueue());
    }

    @Bean
    public Binding binding() {
        return BindingBuilder.bind("default_queue")
                .to("default_exchange")
                .with("default_key");
    }
}
```

## RabbitMQUtils.java

```java
import com.rabbitmq.client.Channel;
import org.slf4j.Logger;

import java.io.IOException;

public final class RabbitMQUtils {

    public static void askMessage(Channel channel, long tag, final Logger logger) {
        askMessage(channel, tag, logger, false);
    }

    public static void askMessage(Channel channel, long tag, final Logger logger, boolean multiple) {
        try {
            channel.basicAck(tag, multiple);
        } catch (IOException e) {
            logger.error("RabbitMQ，IO异常，异常原因为：{}", e.getMessage());
        }
    }

    public static void rejectMessage(Channel channel, long tag, final Logger logger) {
        rejectMessage(channel, tag, logger, false, false);
    }

    public static void rejectAndBackMQ(Channel channel, long tag, final Logger logger) {
        rejectMessage(channel, tag, logger, false, true);
    }

    public static void rejectMessage(Channel channel, long tag, final Logger logger, boolean multiple, boolean request) {
        try {
            channel.basicNack(tag, multiple, request);
        } catch (IOException e) {
            logger.error("RabbitMQ，IO异常，异常原因为：{}", e.getMessage());
        }
    }
}
```

## 生产者生产消息

>   SendMessageController.java

```java
import java.io.UnsupportedEncodingException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;
import java.util.Map;

import com.fasterxml.jackson.databind.ObjectMapper;

import org.dom4j.DocumentException;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
 
@RestController
public class SendMessageController {
 
    @Autowired
    RabbitTemplate rabbitTemplate;

    @Autowired
    ObjectMapper mapper;

    @GetMapping("/sendDirectMessage")
    public String sendDirectMessage(int msgID, String msgData) {
        String createTime = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
        Map<String,Object> map=new HashMap<>();
        map.put("msgID",msgID);
        map.put("msgData",msgData);
        map.put("createTime",createTime);

        //将消息携带绑定键值：TestDirectRouting 发送到交换机TestDirectExchange
        rabbitTemplate.convertAndSend("default_exchange", "default_key", map);
        
        return "ok";
    }

}
```

## 消费者消费

>   MQConsumerService.java

```java
import java.io.UnsupportedEncodingException;
import java.util.Map;

import com.my.project.util.RabbitMQUtils;
import com.rabbitmq.client.Channel;

import org.dom4j.DocumentException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.amqp.support.AmqpHeaders;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.handler.annotation.Header;
import org.springframework.stereotype.Service;

@Service
public class MQConsumerService {
    private static final Logger LOGGER = LoggerFactory.getLogger(MQConsumerService.class);

    @RabbitListener(queues = "default_queue")
    public void receive(Map<String, Object> map, Channel channel,
            @Header(AmqpHeaders.DELIVERY_TAG) long tag) {

        LOGGER.info("In Queue: {}", map);
        // do something
        LOGGER.info("消费结束, 手动确认!");
        RabbitMQUtils.askMessage(channel, tag, LOGGER);
    }
}
```

## 安装插件步骤

> 安装延时插件(rabbitmq_delayed_message_exchange)

-   下载插件

https://github.com/rabbitmq/rabbitmq-delayed-message-exchange/releases/tag/3.9.0

-   复制进容器

```bash
docker cp rabbitmq_delayed_message_exchange-3.9.0.ez rabbitmq_server:/opt/rabbitmq/plugins
```

-   进入容器

```bash
docker exec -it rabbitmq_server /bin/bash
```

-   启用插件

```bash
cd /opt/rabbitmq/plugins
rabbitmq-plugins enable rabbitmq_delayed_message_exchange
```

-   查看安装是否成功

```bash
rabbitmq-plugins list
# 查找是否有rabbitmq_delayed_message_exchange状态是[E*]
```

## 注意事项

### 1. 保证消息不被重复消费

① 给消息做一个唯一的主键，那么就算出现重复消费的情况，就会导致主键冲突，避免数据库出现脏数据。

② 消费者函数的幂等性。

③ 如果上面两种情况还不行，上大招。准备一个第三方介质，来做消费记录。以redis为例，给消息分配一个全局id，只要消费过该消息，将<id,message>以K-V形式写入redis.那消费者开始消费前，先去redis中查询有没有消费记录即可。

### 2. 保证消费的可靠性传输

持久化队列：durable=true and deliveryMode=2

队列防丢：采用手动确认消息即可

## 问题列表：

### 1. 为什么要使用消息队列

解耦、异步、削峰。

解耦：比如发订单创建给用户发短信。

异步：将消息写入消息队列，非必要的业务逻辑以异步的方式运行，加快相应速度

削峰：慢慢的按照数据库能处理的并发量，从消息队列中慢慢拉取消息。在生产中，这个短暂的高峰期积压是允许的。

### 2. 使用消息队列会有的缺点

系统可用性会降低：本来其他系统只要运行好好的，那你的系统就是正常的。现在你非要加入个消息队列进去，那消息队列挂了，你的系统不是呵呵了。

系统复杂性增加：加入了消息队列，要多考虑很多方面的问题，比如：一致性问题、如何保证消息不被重复消费、如何保证消息可靠性传输等

### 3. 为什么是rabbitmq

rabbitmq吞吐虽然弱于kafka，但是功能完善，容易管理。

