#oct to dec.py
n=input("Enter octal number :")
oct=0
a=n[::-1]
for i in range(len(a)):
    if (a[i] == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7):
        oct=oct+(8**i)*(int(a[i]))
print(oct)
