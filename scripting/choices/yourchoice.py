#!/usr/bin/env python3.10

import socket
import re
from rich.console import Console

if __name__ == '__main__':
    cons = Console()
    TARGET = ('your_choice.ctf.fifthdoma.in', 8657)

    # String to search for.
    yes = re.compile(r'(\d) \[Yes\]')
    crib = re.compile(r'flag{.*}')

    # Context manager for the spinner and the socket
    with (
        socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s,
        cons.status(
            "Hacking the [green italic]mainframe[/green italic]...",
            spinner='aesthetic'
        ) as status,
    ):
        # Connect to the target
        s.connect(TARGET)
        # initialize the string.
        out_string = ''

        # use the crib to find a flag.
        while crib.search(out_string) == None:
            # Get response from server
            # then decode the bytes
            rcv = s.recv(2048).decode()

            # Find which number to return
            num = yes.findall(rcv)
            
            # Send the number, with a new line character to end!
            s.send(f'{num[0]}\n'.encode())

            # Append the character the server sends
            out_string += s.recv(1).decode()
        
        # Return the found output
        cons.print(out_string)