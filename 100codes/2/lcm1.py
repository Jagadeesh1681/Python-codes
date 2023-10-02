#lcm1.py
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
c=list()
for i in range(1,min(a,b)+1):
	if (a%i==0) and (b%i==0):
		hcf=i
lcm=(a*b)/hcf
print("LCM Of {} , {} = {}".format(a,b,lcm))
