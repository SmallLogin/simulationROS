#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re,socket               # 导入 socket 模块
 
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口号
ADDR = (host, port)

def tcpServer():
    # TCP服务
    # with socket.socket() as s:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 绑定服务器地址和端口
        s.bind(ADDR)
        # 启动服务监听
        s.listen(3)
        print('Waitting for connnecting')
        while True:
            # 等待客户端连接请求,获取connSock
            conn, addr = s.accept()
            print('{} Connected!'.format(addr))
            with conn:
                while True:
                    # 接收请求信息
                    data = conn.recv(1024)
                    if data:
                        endata = data.decode('utf-8')
                        subdata = re.findall(r'\[\d+\]\[\d+\]', endata)
                        if subdata:
                            # if len(subdata) == 0:
                            usefuldata = [int(subdata[0].split('][')[0][1:]), int(subdata[0].split('][')[1][:-1])]
                            print('Received data:', usefuldata)
                            
                            # Center in usefuldata with list 
                            # Calculate IT2FS
                            # Send  IT2FS's return value
                            # s.sendall()
                       
            s.close()

def main():
    tcpServer()

if __name__ == '__main__':
    main()
 
