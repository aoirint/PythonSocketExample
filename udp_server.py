# https://docs.python.org/ja/3/library/socket.html

import socket

HOST = '127.0.0.1'
PORT = 31415

with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as sock:
    sock.bind((HOST, PORT))

    while True:
        binary_data, client_addr = sock.recvfrom(1024)
        if not binary_data: break

        data = binary_data.decode('utf-8')
        print(f'Received from {client_addr}: {data}')

        message = 'こんにちは、世界 🌏'
        binary_message = message.encode('utf-8')
        sock.sendto(binary_message, client_addr)
