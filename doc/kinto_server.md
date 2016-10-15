# kinto
作为本地存储服务，可以在web里直接使用，当做本地云

# 依赖
```
#使用redis作为存储后端
sudo apt-get install redis-server
```

# 使用
```
pip install kinto
kinto init
kinto migrate
kinto start
```

# 配置文件
配置存储后端：http://kinto.readthedocs.io/en/stable/core/storage.html?highlight=redis

当前目录下的config是kinto init自动生成 

# 使用
url：http://192.168.0.121:8888/v1/

https://github.com/Kinto/kinto-admin 源码 压缩完只有一个文件：view-source:https://kinto.github.io/kinto-admin/#/?_k=gutlgv

# client
*  kinto.js
*  kinto.py
*  auth: hostname/hostname (wwjpi)
