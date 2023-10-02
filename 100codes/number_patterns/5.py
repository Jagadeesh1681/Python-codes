n=int(input("Enter a  number :"))
k=10
for i in range(n):
	for j in range(n-i):
		print(k , end="")
		k=k-1
	print()
