#!/usr/bin/env python3.10

import base64

if __name__ == '__main__':
    encodedText = ''
    with open ('multiplex_encoded.txt') as b64:
        # Puts all of the base64 into a single string
        text = ''.join(b64.readlines())

    # Attack with a crib of flag.
    while 'flag' not in text:
        text = base64.b64decode(text).decode()
    
    print(f'The flag is {text}')
