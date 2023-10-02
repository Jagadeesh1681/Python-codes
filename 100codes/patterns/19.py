n=int(input("Enter no.of rows :"))
a=(2*n)+1
for i in range(1,n+1):
    if (i == 1):
        print(" "*(a-i) + "* "*i)
    else:
        print(" "*(a-i) + "*" + " "*(2*i-3) + "*")
