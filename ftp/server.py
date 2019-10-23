# server
import sys
import socket
import random
import os.path as path

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('usage: ftp.py <port>')
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

            data = client.recv(1024).decode('utf-8').strip()
            if not data:
                continue

            ftp_port = random.randint(9000, 10000)
            file_path = '/var/www/files/' + data
            file_path = path.realpath(file_path)

            if file_path.startswith('/var/www/files/') and file_path.isfile(file_path):
                client.send(str(ftp_port).encode('utf-8'))

                ftp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                ftp_sock.bind(("0.0.0.0", ftp_port))
                ftp_sock.listen(1)
                ftp_client, ftp_addr = ftp_sock.accept()
                file_data = open(file_path, 'rb').read()
                ftp_client.send(file_data)
                ftp_client.close()
            else:
                client.send("0".encode('utf-8'))
            client.close()
    except KeyboardInterrupt:
        sock.close()
        ftp_sock.close()
        exit(0)