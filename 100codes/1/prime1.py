#prime1.py
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
for i in range(a,b+1):
    x=0
    for j in range(2,i):
        if (i%j == 0):
            x=x+1
            break
    if (x == 0):
        print(i)
            
