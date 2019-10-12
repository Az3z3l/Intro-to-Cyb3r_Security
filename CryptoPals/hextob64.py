import codecs

hex=input()
b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
print(b64)