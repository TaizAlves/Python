maior = None
menor = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        num=int(num)
    except:
        print('Invalid input')
    else:
        if menor is None:
            menor= num
        elif num < menor:
            menor= num
        if maior is None:
            maior=num
        elif num > maior:
            maior =num
print("Maximum is", maior)
print('Minimum is', menor)
