# bin to dec.py
n=input("Enter binary number :")
dec=0
a=n[::-1]
for i in range(len(a)):
    if (a[i] == 0 or 1):
        dec=dec+(2**i)*(int(a[i]))
print(dec)
