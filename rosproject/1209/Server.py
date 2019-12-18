#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re,socket               # 导入 socket 模块
import sys
sys.path.append("/home/smalllogo/tracking_ws/src/uav_follow_robot/scripts/1209/PyIT2FLS-master/PyIT2FLS-master/examples")
from new_v1 import IT2FL_v1_fun
from new_v2 import IT2FL_v2_fun

 
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
                            # print('Received data:', usefuldata)
                            # print('Received data:', usefuldata[1])
                            # Center in usefuldata with list 
                            # Calculate IT2FS
                            # IT2FL_fun(0.8,0.6)
                            w=752
                            h=480
                            
                            y=(usefuldata[1]-h/2)/(h/2)
                            print("v1_input:",y)
                            IT2FL_v1_fun(y)

                            x=(int(usefuldata[0])-w/2)/(w/2)
                            print("v2_input:",x)
                            IT2FL_v2_fun(x)

                            # x2=(int(usefuldata[0])-w/2)/(w/2)
                            # y2=(int(usefuldata[1])-h/2)/(h/2)
                            # if (abs(x2))**2+(abs(y2))**2 >= (0.4)**2:
                            # if abs(x2)>= 0.3 or  abs(y2)>= (0.3):
                            #     print("v2_input:",x2,y2)        
                            #     IT2FL_v2(x2,y2)
                            # else:
                            #     print("v2=0")
                                                 
                            # Send  IT2FS's return value
                            # s.sendall()
                       
            s.close()

def main():
    tcpServer()

if __name__ == '__main__':
    main()
 
