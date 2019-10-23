# server
import sys
import socket
import random
import os.path as path
import uuid

USERS_DATA = {
    'admin': {
        'password': 'KhkjhUG&*T87ty78G*G',
        'secret_data': 'Some secret data belonging to admin.'
    },
    'user': {
        'password': 'easy',
        'secret_data': 'Some secret data belonging to user.'
    },
}

SESSIONS = {}
NEXT_SESION_ID = 0

SEPARATOR = b'\n'


# login LOGIN:PASSWORD
# data SESSION_ID
# logout SESSION_ID

def recv_until(sock, sep):
    data = bytes()
    while data[-len(sep):] != sep:
        data += sock.recv(1)
    return data[:-len(sep)]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('usage: data-server.py <port>')
        print("No args")
        exit(1)

    port = int(sys.argv[1])

    try:
        int(sys.argv[1])
        assert 0 < port < 65535
    except ValueError:
        sys.stderr.write('usage: ftp.py <port>')
    except AssertionError:
        sys.stderr.write('invalid port')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", port))
    sock.listen(10)
    try:
        while True:
            client, addr = sock.accept()

            data = recv_until(client, SEPARATOR).decode('utf-8')
            cmd = data.split(' ')[0].lower()

            if cmd == 'login':
                if len(data.split(' ')) < 2:
                    client.send(b'Wrong command\n')
                elif len(data.split(' ')[1].split(':')) < 2:
                    client.send(b'Wrong command\n')
                l, p = map(lambda x: x.strip(), data.split(' ')[1].split(':'))
                if l not in USERS_DATA or USERS_DATA[l]['password'] != p:
                    client.send(b'Invalid credentials\n')
                else:
                    #session_id = NEXT_SESION_ID
                    #NEXT_SESION_ID += 1

                    session_id = uuid.uuid4()
                    SESSIONS[session_id] = l
                    client.send('OK SessionID {}\n'.format(str(session_id)).encode('utf-8'))
            elif cmd == 'data':
                if len(data.split(' ')) < 2:
                    client.send(b'Wrong command\n')
                else:
                    session_id = data.split(' ')[1]
                    if not session_id.isdigit() or int(session_id) not in SESSIONS:
                        client.send(b'Invalid session\n')
                    else:
                        l = SESSIONS[int(session_id)]
                        d = USERS_DATA[l]['secret_data']
                        client.send(d.encode('utf-8'))
                        client.send(b'\n')
            elif cmd == 'logout':
                if len(data.split(' ')) < 2:
                    client.send(b'Wrong command\n')
                else:
                    session_id = data.split(' ')[1]
                    if not session_id.isdigit() or int(session_id) not in SESSIONS:
                        client.send(b'Invalid session\n')
                    else:
                        del SESSIONS[int(session_id)]
                        client.send(b'OK')
            else:
                client.send(b'Wrong command\n')
            client.close()
    except KeyboardInterrupt:
        sock.close()
        exit(0)