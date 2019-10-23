'''
Serwer TCP
'''
# coding=utf-8
import socket
import threading

def fib(n):
    n1 = 0
    n2 = 1
    i  = 1
    while ( i < n ):
        sumOfPrevTwo = n1 + n2;
        n1 = n2;
        n2 = sumOfPrevTwo;
        i += 1
    return n1

def apply(client):
    data = client.recv(1024)
    if not data:
        client.close()
        return
    data = int(data.decode())
    fib_result = str(fib(data))
    client.send(fib_result.encode('utf-8'))
    client.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 1769))
s.listen(5)

threads = []
try:
    while True:
        client, addr = s.accept()
        print("Connected: " + addr[0])
        thread = threading.Thread(target=apply, args=(client,))
        threads.append(thread)
        thread.start()
except Exception as ex:
    for thread in threads:
        thread.join()
finally:
    s.close()