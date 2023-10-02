a=int(input("Enter no.of rows :"))
b=int(input("Enter no.of cols :"))
for i in range(1,a+1):
	for j in range(1,b+1):
		if ( i == 1 or j == 0 or a == 0 ):
			print(3,end="")
		else:
			print(i,end="")
	print()
