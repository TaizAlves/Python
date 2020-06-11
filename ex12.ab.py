#Lesson 12- assignment 3
#The program will use urllib to read the HTML from the data files below,
#extract the href= vaues from the anchor tags, scan for a tag that is in a particular position
#relative to the first name in the list,
#follow that link and repeat the process a number of times and report the last name you find. '''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl




# Ignore SSL certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode = ssl.CERT_NONE

#abrir , ler e preparar com o BeautifulSoup
url=input('Enter url: ')
if len(url) < 1:  url='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html=urllib.request.urlopen(url,context=ctx).read()
soup= BeautifulSoup(html, 'html.parser')

position=int(input('Enter position:  '))-1
times= int(input('Enter loop´s nr: '))
#retorno de valores do marcador 'a'
tag= soup('a')
dado={}
tudo=list()
for v in tag:
    # Look at the parts of a tag
    url= v.get('href', None)
    nome= v.contents[0]
    dado['url']= url
    dado['nome']= nome
    tudo.append(dado.copy())
print(tudo[position]['nome'])
print(tudo[position]['url'])
n=0

while True:
    n += 1
    if n== times:
        break
    # url dentro da url
    url2 = tudo[position]['url']
    html = urllib.request.urlopen(url2, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # retorno de valores do marcador 'a'
    tag = soup('a')
    dado = {}
    tudo = list()
    for v in tag:
        # Look at the parts of a tag
        url = v.get('href', None)
        nome = v.contents[0]
        dado['url'] = url
        dado['nome'] = nome
        tudo.append(dado.copy())
    print(tudo[position]['nome'])
    print(tudo[position]['url'])
