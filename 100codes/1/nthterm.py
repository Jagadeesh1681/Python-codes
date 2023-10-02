#nth term of fibonacci series.
n=int(input("Enter a number :"))
n1,n2=0,1
for i in range(2,n+1):
    n3=n1+n2
    n1=n2
    n2=n3
print("{} term of Fibonacci series = {}".format(n,n3))


    

