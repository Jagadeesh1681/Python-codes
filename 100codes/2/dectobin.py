#decimal to binary.py
n=int(input("Enter decimal sys value :"))
a=list()
while (n!=0):
	r=n%2
	n=n//2
	a.append(r)
for j in a[::-1]:
    print(j,end=" ")
