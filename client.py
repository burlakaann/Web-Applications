'''
Klient TCP
'''
# coding=utf-8
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(('localhost', 1769))
    while True:
        data = ("Ania")
        s.send(data[-1].encode('utf-8'))
        data = s.recv(1024)
        if not data:
            break
        data = data.decode('utf-8')
        print(data)
        break;
    s.close()
except socket.error:
    print ('Error')