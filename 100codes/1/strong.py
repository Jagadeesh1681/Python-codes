#strong.py
n=int(input("Enter a number :"))
a=str(n)
b=len(a)
sum=1
num=0
for i in range(b):
    x=1
    while (x<=int(a[i])):
        sum=sum*x
        x=x+1
    num = num + sum
    sum=1
    x=1
if( num == n):
    print("{} is a strong number".format(n))
else:
    print("{} is not a strong number".format(n))
