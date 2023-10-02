n=input("Enter a string :")
n=n.capitalize()
a=list(n)
result=''
for i in range(1,len(a)+1):
    if (a[i-1] == ' '):
        a[i] = a[i].upper()
for j in a:
    print(j,end="")
print()
