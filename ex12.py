import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL  certificados de erros (padrão)
ctx= ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter site: ')  #http://www.dr-chuck.com
html= urllib.request.urlopne(url,context=ctx).read() #faz o pedido, "trata" com o ctx e lê
soup= BeautifulSoup(html, 'html.parser') # volta um txt http tratado

# Retrieve all of the anchor tags - no site os <a/ e vem um outro site ou página
tags= soup('a')
for v in tags:
    print(v.get('href', None))
    
