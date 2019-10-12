cipher=input()

#Positive cipher
for i in range(26):
    flag=''
    for j in cipher:
        if j.isalpha():
            if j.isupper():
                letter=ord(j)-i
                if (letter<=64):
                    letter=26+letter
            else:
                letter=ord(j)-i
                if (letter<=96):
                    letter=26+letter
        else:
            letter=ord(j)    
        flag=flag+chr(letter)
    print("+"+str(i)+"::"+flag)

print()
# Negative cipher
for i in range(26):
    flag=''
    for j in cipher:
        if j.isalpha():
            if j.isupper():
                letter=ord(j)+i
                if (letter>=91):
                    letter=letter-26
            else:
                letter=ord(j)+i
                if (letter>=123):
                    letter=letter-26
        else:
            letter=ord(j)   
        flag=flag+chr(letter)
    print("-"+str(i)+"::"+flag)




#reference ::  https://en.wikipedia.org/wiki/Caesar_cipher
#              https://cryptii.com/pipes/caesar-cipher