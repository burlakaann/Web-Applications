import base64
import socket

source_address = input("Wprowadz adres nadawcy");
destination_adress = input("Wprowadz adres/adresy odbiorów (po przecinku)");
subject = input("Wprowadz temat wiadomości");
email_message = input("Wpisz treść wiadomości");

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('poczta.interia.pl', 587))
print(str(s.recv(2048).decode('utf-8')))
print('\n')

message = 'EHLO ania\r\n'
s.send(message.encode('utf-8'))
print(str(s.recv(2048).decode('utf-8')))
print('\n')

message = 'AUTH LOGIN\r\n'
s.send(message.encode('utf-8'))
print(str(s.recv(2048).decode('utf-8')))
print('\n')

crlmsg = '\r\n'
user = base64.b64encode('anna.burlaka@interia.pl'.encode())
password = base64.b64encode('123456789'.encode())
s.send(user)
s.send(crlmsg.encode('utf-8'))
print(str(s.recv(2048).decode('utf-8')))
print('\n')

s.send(password)
s.send(crlmsg.encode('utf-8'))
print(str(s.recv(2048).decode('utf-8')))
print('\n')

src_addr = 'mail from: <'+source_address+'>\r\n'
s.send(src_addr.encode('utf-8'))
print(str(s.recv(2048)))
print('\n')

dest_addr = 'rcpt to: <'+destination_adress+'>\r\n'
s.send(dest_addr.encode('utf-8'))
print(str(s.recv(2048)))
print('\n')

s.send('data\r\n'.encode('utf-8'))
print(str(s.recv(2048)))
print('\n')

s.send(('To: <'+destination_adress+'>\r\n').encode('utf-8'))

s.send(('From: <'+source_address+'>\r\n').encode('utf-8'))

s.send(('Subject: '+subject+'\r\n\r\n').encode('utf-8'))

s.send(('\r\n'+email_message+'\r\n').encode('utf-8'))

print(str(s.recv(2048)))
print('\n')

s.send("\r\n.\r\n".encode('utf-8'))

s.send("quit\r\n".encode('utf-8'))
print(str(s.recv(2048)))
print('\n')
