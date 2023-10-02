#binary to octal.py
n=input("Enter binary number :")
d=0
a=list()
for i in range(len(n)):
	if (n[i] == 0 or 1):
		d=d+(2**(i+1))*int(n[i])
while(d!=0):
    r=d % 8
    a.append(r)
    d=d//8
for j in a[::-1]:
    print(j,end="")
