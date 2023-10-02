#amstrong1.py
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
for i in range(a,b+1):
    num=0
    c=str(i)
    l=len(c)
    for j in range(l):
        num=num+int(c[j])**l
    if (num == i):
        print(i)
