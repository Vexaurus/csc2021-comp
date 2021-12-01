#!/usr/bin/env python3.10
#%%
import base64
import re
brac
removeme = re.compile(r'<removeme>')
# %%
with open('input4onion.txt', 'r') as origin:
    message = origin.readlines()[0]


# %%
a, b = message.split('-')
# %%
funcs = {
    '64': lambda x: base64.b64decode(x),
}
#%%
x = base64.b64decode(b).decode()
# %%
j = x
# %%
