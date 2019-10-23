'''
Serwer TCP
'''
# coding=utf-8
import socket
import threading
import ssl

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

threads = []
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='C:/Users/Aniuta/server.crt', keyfile='C:/Users/Aniuta/server.key')
context.load_verify_locations(cafile='C:/Users/Aniuta/client.crt')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.bind(("localhost", 1769))
s.listen(5)
ss = context.wrap_socket(s, server_side=True)

try:
    while True:
        conn, addr = ss.accept()
        print("Connected: " + addr[0])
        thread = threading.Thread(target=apply, args=(conn,))
        threads.append(thread)
        thread.start()
except Exception as ex:
    print(ex)
finally:
    for thread in threads:
        thread.join()
    ss.close()

