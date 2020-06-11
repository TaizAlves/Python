name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
txt = open(name)
counts={}
for l in txt:
    if l.startswith('From '):
        line=l.split()
        hrs=line[5]
        hour=hrs.split(':')
        jhour=[hour[0]]
        #print(jhour)
        for n in jhour:
            counts[n]= counts.get(n,0)+1
h= []
for k,v in counts.items():
    lista=(k,v)
    h.append(lista)
h=sorted(h)
for k,v in h:
    print(k,v)
    
