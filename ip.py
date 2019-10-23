import socket
'''
try:
    socket.inet_aton('127.0.0.1')
except socket.error:
    print('niepoprawny ip')

host = socket.gethostbyaddr('127.0.0.1')
print(host)
'''
'''
TCP_IP = 'google.com'
TCP_PORT = 8080

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = s.connect_ex((TCP_IP, TCP_PORT))
    if res == 0:
        print('Udało się')
    else:
        print('Nie udało się')
    s.close()
except socket.error:
    print('Błąd')
'''


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.settimeout(1)
    for i in range(78,82):
        res = s.connect_ex(("google.pl", i))
        if res == 0:
            print('Port ',i, 'is opened')
        else:
            print('Port ',i, 'is closed',)
except socket.error:
    print('Błąd')



