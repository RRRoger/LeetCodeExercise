# FRP内网穿透最简单设置

## 服务端

### 安装

```sh
wget https://github.com/fatedier/frp/releases/download/v0.34.2/frp_0.34.2_linux_amd64.tar.gz

tar zxf frp_0.34.2_linux_amd64.tar.gz

cd frp_0.34.2_linux_amd64/

vim frps.ini 
```

### 配置ini

```ini
[common]
nd_port = 7000
vhost_http_port = 8080
authenticate_new_work_conns = true
authenticate_heartbeats = true
authentication_method = token
token = 123
```

### 启动

```sh
sudo ./frps -c frps.ini
```

## 客户端

### 安装[以Mac为例]

```sh
wget https://github.com/fatedier/frp/releases/download/v0.40.0/frp_0.40.0_darwin_amd64.tar.gz

# 解压

# 修改配置文件
```

#### 配置

```ini
[common]
server_addr = 远程IP
server_port = 7000
authenticate_new_work_conns = true
authenticate_heartbeats = true
authentication_method = token
token = 123

; [ssh]
; type = tcp
; local_port = 22
; remote_port = 6000

[web]
type = http
local_port = 8000
custom_domains = 你要访问的域名
use_compression = true
```

### 启动

```sh
./frpc -c frpc.ini
```

