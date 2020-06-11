txt= input('Enter the file name:')
if len(txt) < 1 :
    txt= "mbox-short.txt"
    fl= open(txt)
    count=0

for l in fl:
    if not l.startswith('From '):
        continue
    count += 1
    l = l.rstrip()
    separ= l.split()
    print(separ[1])
print("There were", count, "lines in the file with From as the first word")
