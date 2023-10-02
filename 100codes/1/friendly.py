#friendly pair.py
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
s1,s2=0,0
for i in range(1,a):
    if (a%i==0):
        s1=s1+i
for j in range(1,b):
    if (b%j==0):
        s2=s2+j
if ((a/s1) == (b/s2)):
    print("{} {} are friendly pair".format(a,b))
else:
    print("{} {} are not a friendly pair".format(a,b))
