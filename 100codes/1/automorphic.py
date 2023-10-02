#Automorphic number.py
n=int(input("Enter a number :"))
a=n**2
if (str(a).endswith(str(n))):
	print("{} is a Automorphic number".format(n))
else:
	print("{} is not a Automorphic number".format(n))
