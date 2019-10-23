'''
Klient TCP
'''
# coding=utf-8
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(('localhost', 1769))
    while True:
        data = input('Podaj liczbę: ')
        s.send(data.encode('utf-8'))
        result = s.recv(1024)
        if not result:
            break
        print("Wynik dla podanej liczby = " + result.decode())
    s.close()
except socket.error as e:
    print('Error')
