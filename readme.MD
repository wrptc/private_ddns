# 动态hosts(私有动态ddns)
私有域名就是在只有自己的私域可用的域名。 \
通过自建服务，实现本机hosts的动态更新，将私有域名解析到客户端当前的ip地址
该工具分为客户端与服务端
- 客户端通过公网服务获取自身ip后发送请求给服务端，要求服务端更新hosts
- 服务端获取来自客户端的请求后更新服务端本机hosts文件实现私有域名的解析
## 服务端
- 依赖python环境

```
sudo apt update
sudo apt install python3
sudo apt install python3-pip
pip3 install flask
```
- 修改config.json文件

```
{
    "sudo_passwd": "你的sudo密码",
    "hosts": "/etc/hosts"  # 一般不用修改
}
```
- 运行app.py

```
python3 app.py
```
- 或后台运行
```
nohup python3 app.py &
```
## 客户端
修改client.sh文件

```
HOST="你的私有域名"
SERVER="http://localhost:5000/hosts"  # 需根据实际情况填写服务端的地址与端口
```
- 执行客户端

```
sh client.sh
```
- 或添加到定时任务

```
*/5 * * * * /path/to//client.sh
```

