# https://docs.python.org/ja/3/library/socket.html
# https://qiita.com/note-tech/items/c3e1e497d231ea1e7ca7

import socket

HOST = '127.0.0.1'
PORT = 31415

with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as sock:
    message = 'Hello, world 🌍'
    binary_message = message.encode('utf-8')

    sock.sendto(binary_message, (HOST, PORT))

    binary_data, server_addr = sock.recvfrom(1024)

data = binary_data.decode('utf-8')

print(f'Received from {server_addr}: {data}')
