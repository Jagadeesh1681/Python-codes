#expressing a number as sum of 2 prime numbers.
n=int(input("Enter a number :"))
a=list()
for i in range(2,n+1):
    x=0
    for j in range(2,i):
        if (i%j == 0):
            x=x+1
            break
    if (x == 0):
        a.append(i)
for k in range(len(a)):
    for l in range(k+1,len(a)):
        if (a[k]+a[l] == n):
            print("{} can be expressed as sum of {} , {}.".format(n,a[k],a[l]))
            break

    
