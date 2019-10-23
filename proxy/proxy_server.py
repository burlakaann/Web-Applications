'''
Serwer TCP
'''
# coding=utf-8
import socket, sys
#rapsocket -serwer

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", int(sys.argv[1])))
s.listen(5)

proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy.connect((socket.gethostbyname(sys.argv[2]), int(sys.argv[3])))

def get_content_length(response):
    if response:
        index = response.index(b'Content-Length: ')
        if index:
            data = response[(index + len(b'Content-Length: ')):]
            length = int(data[0:data.index(b'\r\n')])
            return length
    return 0

while True:
    client, addr = s.accept()
    print("Connected: " + addr[0])

    data = client.recv(1024)
    while data and b'\r\n\r\n' not in data[-4:]:
        data += client.recv(1024)
    print(data.decode())
    proxy.sendall(data)

    data = proxy.recv(1024)
    content_length = get_content_length(data)
    while len(data) <= content_length:
        data += proxy.recv(1024)
        content_length = get_content_length(data)
    print(content_length)

    client.sendall(data)

    client.close()

proxy.close()
s.close()
