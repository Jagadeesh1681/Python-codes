n=int(input("Enter no.of rows :"))
a=(n+1)*2
for i in range(1,a-1,2):
	print(" "*(a-i) + "* "*(i))
