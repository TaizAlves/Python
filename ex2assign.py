import urllib.request, urllib.parse, urllib.error
import json
import ssl


ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


site=  'http://py4e-data.dr-chuck.net/comments_368552.json'
html= urllib.request.urlopen(site, context=ctx).read()

soma=0
todo=json.loads(html)
#print(todo)
print(todo['comments'])
print('Count: ', len(todo['comments']))
for v in todo['comments']:
    #print(v['count'])
    soma+= v['count']
print('SUM:', soma)



