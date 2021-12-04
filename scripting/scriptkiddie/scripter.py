#!/usr/bin/env python3.10

if __name__ == '__main__':
    # Decoded from online source.
    # Open the input file:
    with open('./decoded.txt', 'r') as inp:
        text = inp.read()

    # initialize the count
    count = {}
    
    # loop through all characters and count frequency.
    for char in text:
        count[char] = count.get(char, 0) + 1
    
    # return the count.
    print(count)