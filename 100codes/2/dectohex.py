#decimal to hexadecimal.py
n=int(input("Enter dec sys value :"))
a=list()
while (n!=0):
    r=n%16
    n=n//16
    if (r <10):
        a.append(chr(r+48))
    else:
        a.append(chr(r+55))
for i in a[::-1]:
    print(i , end="")
