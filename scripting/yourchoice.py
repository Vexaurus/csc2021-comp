#!/usr/bin/env python3.10

from ast import Num
import socket
import re

TARGET = ('your_choice.ctf.fifthdoma.in', 8657)

yes = re.compile(r'(\d) \[Yes\]')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(TARGET)
    o = []
    try:
        for _ in range(10000):
            
            rcv = s.recv(2048).decode()
            num = yes.findall(rcv)
            print(rcv)
            s.send(num[0].encode())
            s.send('\n'.encode())
            o.append(s.recv(1).decode())
    except:
        print(''.join(o))