import re
soma=count=0
name=input('Enter document name: ')
if len(name)<1 :name= "regex_sum_368547.txt"
txt= open(name)
for line in txt:
    line=line.rstrip()
    num= re.findall('[0-9]+',line)
    if len(num) < 1: continue
    for v in num:
        v= int(v)
        soma+=v
        count+=1
    print(v)
print('total', soma)
print('quantidade:', count)
