def computepay(h,r):
    hora=float(h)
    rata=float(r)
    if hora <=40:
        pay=hora*rata
    else:
        extra=hora-40
        rateeh=rata*1.5
        pay=(40*rata)+(rateeh*extra)
    return pay

hrs = input("Enter Hours:")
rate=input('Enter Rate: ')
p = computepay(hrs,rate)
print(p)
