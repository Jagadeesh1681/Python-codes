#Fibonacci Series upto nth term.
n=int(input("Enter a number :"))
n1,n2=0,1
print("Fibonacci series:",n1,n2,end=" ")
for i in range(2,n+1):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
print()
    

