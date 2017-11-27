#first three lines are basically cut and paste
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)


#now to receive the data

while True:
    data = mysock.recv(512)
    if (len(data) <1):
        break
    print(data.decode())

#close the socket
mysock.close()
