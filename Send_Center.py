#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py
 
import socket               # 导入 socket 模块
 
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口号
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect((host,port))

def send_center(x,y):
    message = str(str([x])+str([y]))
    clientsocket.sendall(message.encode('utf-8'))
    print "Send Success!"

    # Receive Code
    # return




# def main():
#     while True:
#         send_center(1,2)

# if __name__ == '__main__':
#     main()