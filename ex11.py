import re
numlist=list()
count={}
name=input('Enter document name: ')
if len(name)<1 :name= "mbox-short.txt"
txt= open(name)
for line in txt:
    line= line.rstrip()
    nrspam= re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line) # procurar e voltar valores que comecem (^) com DSPAM-Confidence:   depois tenham nr {0-9.) 1 ou mais (+)
    if len(nrspam)<1: continue  #se não tiver, continue Para não dar bag
    nrspam=float(nrspam[0])
    numlist.append(nrspam) #coloquei em uma lista(para esseexemplo nem precisava)
    count[nrspam]=count.get(nrspam,0)+1 #contei quantos tem que cada e coloquei dentro de um dicionário

for k,v in count.items():
    print('Seguem os números: ',k,'e quantidade encontrada = ',v)
print('O total encontrado foi de :',len(count))
print(numlist)
