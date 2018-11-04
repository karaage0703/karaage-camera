# -*- coding:utf-8 -*-
import socket

host = "karaMac.local"
port = 8888

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port)) 

def communicate(filename):
    print(filename)
    client.send(b'go')
    rcvmsg = client.recv(4096)
    print(rcvmsg)
    if rcvmsg == b'ok':
        client.send(filename)

        response = client.recv(4096)
        print(response)

        response = client.recv(4096)
        print(response)

if __name__ == '__main__':
    communicate()
