fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('The is no such file. Try again!')
    quit()
cont=0
tnum=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    cont+=1
    onde=line.find(':')
    num=line[onde+2:].rstrip()
    print(num)
    num=float(num)
    tnum += num
    num=0
print(f'Average spam confidence: {tnum/cont}')
