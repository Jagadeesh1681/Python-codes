#Highest Common Factor.py
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
for i in range(1,min(a,b)+1):
	if (a%i==0) and (b%i==0):
		hcf=i
print(hcf)
