import urllib.request, urllib.parse,urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode= ssl.CERT_NONE

site= ' http://py4e-data.dr-chuck.net/comments_368551.xml'
html=urllib.request.urlopen(site,context=ctx).read()

print(html.decode()) # volta em forma de'arvore'
soma=0
tree= ET.fromstring(html)  #Aqui NÃO pode estar com DECODE
all= tree.findall('comments/comment')
for item in all:
    count=item.find('count').text
    count=int(count)
    soma+= count
print(soma)
