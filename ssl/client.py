'''
Klient TCP
'''
# coding=utf-8
import socket
import ssl
hostname = 'localhost'

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile='C:/Users/Aniuta/server.crt')
context.load_cert_chain(certfile='C:/Users/Aniuta/client.crt', keyfile='C:/Users/Aniuta/client.key')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
ss = context.wrap_socket(s, server_hostname=hostname)
try:
    ss.connect((hostname,1769))
    while True:
        data = input('Podaj liczbę: ')
        ss.send(data.encode('utf-8'))
        result = ss.recv(1024)
        if not result:
            break
        print("Wynik dla podanej liczby = " + result.decode())
    ss.close()
except socket.error as e:
    print(e)
