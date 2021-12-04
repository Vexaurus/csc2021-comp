import base64

encodedText = ''
with open ('multiplex_encoded.txt') as b64:
    text = b64.readlines()
    encodedText = ''.join(text)

#print(encodedText)

decodedText = encodedText

##QUICK and dirty
while 'flag' not in str(decodedText): # OR decodedText != '':
    decodedText = base64.b64decode(decodedText)
    
print(decodedText)
