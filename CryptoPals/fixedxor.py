import binascii

fixed="686974207468652062756c6c277320657965"

cipher=input()

print("Key used is '686974207468652062756c6c277320657965'\n")

cip=bytearray.fromhex(cipher)
key=bytearray.fromhex(fixed)
plaintext=bytearray(len(cip))

for i in range(len(cip)):
    plaintext[i]=cip[i]^key[i]

plaintext=binascii.hexlify(plaintext)
print(plaintext)