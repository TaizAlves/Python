# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('The is no such file. Try again!')
    quit()
for line in fh:
    line=line.rstrip().upper() # tira o espaço 'duplo'
    print(line)
