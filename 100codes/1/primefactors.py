#prime factors.py
n=int(input("Enter a number :"))
a=list()
b=list()
for i in range(2,(n//2+1)):
    if (n % i == 0):
        a.append(i)
if a[0] == 2:
    b.append(2)
    a.remove(2)
for j in a:
    f=0
    for k in range(2,j):
        if (j%k==0):
            f=f+1
    if (f == 0):
        b.append(j)
print(b)
    
