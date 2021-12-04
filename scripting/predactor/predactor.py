#!/usr/bin/env python3.10

import re
import socket
import random
from rich.console import Console

if __name__ == '__main__':
    # Generate a console
    cons = Console()

    # Set the target
    TARGET = ('predactor.ctf.fifthdoma.in', 2785)
    
    # Set the Crib to look for.
    CRIB = re.compile(r'flag{.*}')

    # Set context manager for socket and spinner.
    with (
        socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s,
        cons.status(
            "Predicting the predictor...",
            spinner="arrow3"
        )
    ):
        # Connect to the target
        s.connect(TARGET)
        # Get the inital response from the server
        response = s.recv(2048).decode()
        
        # Search using the crib for a flag
        while CRIB.search(response) == None:
            # Spam the server with a random integer
            s.send(f'{random.randint(0, 9)}\n'.encode())
            
            # Await server response
            response = s.recv(2048).decode()

        # Return flag to user.
        cons.print(response)