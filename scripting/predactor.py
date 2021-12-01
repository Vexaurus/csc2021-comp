#!/usr/bin/env python3.10

import socket
import re
import random
import time

TARGET = ('predactor.ctf.fifthdoma.in', 2785)

yes = re.compile(r'(\d) \[Yes\]')

nums = [*range(0,10)]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(TARGET)
    r = s.recv(2048).decode()
    print(r)
    num = random.choice(nums)
    print("Sending: "+ str(num))
    s.send(f'{num}\n'.encode())
    r = s.recv(128).decode()
    print(r)
    while 'flag' not in r:
        if 'Incorrect' in r:
            nums = [*range(0,10)]
        else:
            nums.remove(num)

        num = random.choice(nums)
        time.sleep(0.1)
        print("Sending: "+ str(num))
        s.send(f'{num}\n'.encode())
        r = s.recv(128).decode()
        print(r)
