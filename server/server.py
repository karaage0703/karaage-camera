# -*- coding:utf-8 -*-
import socket
import subprocess
import time

host = "karaMac.local" #お使いのサーバーのホスト名を入れます
port = 8888 #クライアントと同じPORTをしてあげます

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind((host,port)) #IPとPORTを指定してバインドします
serversock.listen(10) #接続の待ち受けをします（キューの最大数を指定）

print('Waiting for connections...')
try:
    clientsock, client_address = serversock.accept() #接続されればデータを格納

    while True:
        rcvmsg = clientsock.recv(1024)
        print('Received -> %s' % (rcvmsg))
        if rcvmsg == '.':
            break
        if rcvmsg == b'go':
            print('go')
            clientsock.send(b'ok')
            photo_name = clientsock.recv(1024)
            photo_name = photo_name.decode()
            print("photo_name=" + photo_name)
            print ("uploading...")
            cmd = "./download.sh " + photo_name
            subprocess.call(cmd, shell=True)

            print("processing...")
            cmd = "./deeplearning.sh " + photo_name
            subprocess.call(cmd, shell=True)

            clientsock.send(b'processed')
            time.sleep(1.0)

            print("downloading...")
            cmd = "./upload.sh "
            subprocess.call(cmd, shell=True)
            clientsock.send(b'uploaded')

except KeyboardInterrupt:
    print('Interrupt!')
    serversock.close()
