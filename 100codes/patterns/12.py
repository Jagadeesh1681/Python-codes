n=int(input("Enter no.of rows :"))
a=(2*n)+1
for i in range(1,n+1):
    print( " "*(n+i) + "*"*(a-2*i))
