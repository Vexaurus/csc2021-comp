#!/usr/bin/env python3.10

import socket
import re

TARGET = ('predactor.ctf.fifthdoma.in', 2785)

yes = re.compile(r'(\d) \[Yes\]')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(TARGET)
    r = s.recv(2048).decode()
    print(r)
    num = 1
    s.send(f'{num}\n'.encode())
    r = s.recv(128).decode()
    print(r)
