#armstrong.py
n=int(input("Enter a number :"))
a=str(n)
l=len(a)
num=0
for i in range(l):
	num=num+int((a[i]))**l
if (n == num):
	print("{} is a Armstrong number".format(n))
else:
	print("{} is not a Armstrong number".format(n))
