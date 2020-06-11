fname = input("Enter file name: ")
fh = open(fname)
separado = list()
for line in fh:
    nline= line.rstrip()
    piece=nline.split()
    for w in piece:
        if w not in separado:
            separado.append(w)
separado.sort()
print(separado)



    
