name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
txt = open(name)
count={}
for l in txt:
    if l.startswith('From '):
        line=l.split()
        sender=[line[1]]
        #print(sender)
        for n in sender:
            count[n] = count.get(n,0)+1
           # print(count)
maior=None
email=None
for k,v in count.items():
    if maior is None or v > maior:
        email= k
        maior= v
print(email, maior)