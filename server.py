'''
Serwer TCP
'''
# coding=utf-8
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 1769))
s.listen(5)
plec = ""
while True:
    client, addr = s.accept()
    print("Connected: " + addr[0])

    while True:
        data = client.recv(1024)
        print(data.decode('utf-8'))
        if not data:
            break;
        if data is "a":
            plec = "zenskie"
        else:
            plec = "meskie"

        client.send(plec.encode('utf-8'))

    client.close()

s.close()