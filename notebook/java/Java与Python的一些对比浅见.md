# Java与Python的一些对比的个人浅见

### 1. springboot+maven构建项目体验比python的一些框架好很多

java的生态确实比其他语言要好很多很多。

### 2. java的重载(overload)编码体验 不如 python的参数默认值

```java
void say(){
  System.out.println("Hello!");
}

void say(String info){
  System.out.println(info);
}
```

```python
def say(info=None):
  if info:
    print(info)
  else:
    print("Hello")
```

比如中间需要新增一个参数，java改起来会比python麻烦，不知道有什么好的写法

### 3. java的多行字符串书写体验不如python

```java
String multiLine = "a\nb\nc";
```

```python
multiLine = """a
b
b"""
```

在sql时可读性和编写体验均不如python的多行字符

### 4. java的规范要比python好

比如封装，集成，多态的，java bean，重载，重写，接口实现都很注重。

python表现的不那么明显。