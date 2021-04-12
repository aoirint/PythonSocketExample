# https://docs.python.org/ja/3/library/socket.html

import socket

HOST = '127.0.0.1'
PORT = 31415

with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(1)

    while True:
        conn, client_addr = sock.accept()
        with conn:
            print(f'Connected by {client_addr}')

            while True:
                binary_data = conn.recv(1024)
                if not binary_data: break

                data = binary_data.decode('utf-8')
                print(f'Received from {client_addr}: {data}')

                message = 'こんにちは、世界 🌏'
                binary_message = message.encode('utf-8')
                conn.sendall(binary_message)
