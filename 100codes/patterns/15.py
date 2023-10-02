n=int(input("Enter no.of rows :"))
a=(2*n)
b=a//2
for i in range(1,a):
	if (i <= b):
		print(" "*(b-i) + "*"*i)
	else:
		print(" "*(i-b) + "*"*(a-i))
