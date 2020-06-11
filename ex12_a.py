from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
soma=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url)<1 : url= 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
btitle = soup('tr')
for v in btitle:
    line=v.decode().split()
    num = re.findall('[0-9]+', line[1])
    if len(num) < 1: continue
    for v in num:
        v = int(v)
        soma += v
    print(v)
print(soma)
