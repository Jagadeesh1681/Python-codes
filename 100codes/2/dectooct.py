#decimal to octal.py
n=int(input("Enter decimal sys value :"))
a=list()
while (n!=0):
	r=n%8
	n=n//8
	a.append(r)
for j in a[::-1]:
    print(j,end=" ")
