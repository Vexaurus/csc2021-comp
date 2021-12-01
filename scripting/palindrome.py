#!/usr/bin/env python3.10

import json
import base64
import concurrent.futures
from rich.progress import track

def is_palindrome(string):
    return string == string[::-1]

def find_pal(string, start, end):
    # base case
    if end - start <= 1:
        return (start, end)
    # if a palindrome shows:
    elif string[start] == string[end]:
        # check if its substring is a palindrome also
        next_pal = find_pal(string, start + 1, end - 1)
        if next_pal == (start + 1, end - 1):
            # if it is, then return the longer
            return (start, end)
        else:
            # if it is not, still return any smaller palindrome in string
            return next_pal
    else:
        # if this string is not a palindrome, check for a smaller in a  substring
        next_pal1 = find_pal(string, start + 0, end - 1)
        next_pal2 = find_pal(string, start + 1, end - 0)
        if next_pal1[1] - next_pal1[0] > next_pal2[1] - next_pal2[0]:
            return next_pal1
        else:
            return next_pal2


def find_greatest_pal(string):
    pal_pair = find_pal(string, 0, len(string)-1)
    return string[pal_pair[0]:pal_pair[1]+1]


print(find_greatest_pal("forgeeksskeegfor"))
o = []
with open('palindrome.txt', 'r') as palin:
    p = palin.readlines()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for j in track(p, description='Finding the good stuff'):
            # print(j.lower())
            r = executor.submit(find_greatest_pal, j.lower())
            x = r.result()
            if len(x) > 5:
                o.append(x)
                print(o[-1])

print(o)