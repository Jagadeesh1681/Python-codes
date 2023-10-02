a=int(input("Enter no.of rows :"))
b=int(input("Enter no.of cols :"))
for i in range(1,a+1):
	if (i == 1 or i == a):
		print("*"*b)
	else:
		print("*" + (" ")*(b-2) + "*")
