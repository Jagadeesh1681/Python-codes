n=int(input("Enter a number :"))
a=(2*n)+1
for i in range(1,a-1):
    if (i <= (a//2)):
        print(" "*(i) + "*"*(a-2*i))
    else:
        print(" "*(a-i-1) + "*"*(2*(i+1)-a))
