hrs = input("Enter Hours:")
h = float(hrs)
rate=input('Enter rate:')
rate= float(rate)
if h <= 40:
    pay=h*rate
else:
    eh=h-40
    rateeh=rate*1.5
    pay=(40*rate)+(eh*rateeh)
print(pay)
