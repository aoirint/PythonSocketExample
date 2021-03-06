# https://docs.python.org/ja/3/library/socket.html

import socket

HOST = '127.0.0.1'
PORT = 31415

with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    message = 'Hello, world 🌍'
    binary_message = message.encode('utf-8')
    sock.sendall(binary_message)

    binary_data = sock.recv(1024)

data = binary_data.decode('utf-8')

print(f'Received from {(HOST, PORT)}: {data}')
