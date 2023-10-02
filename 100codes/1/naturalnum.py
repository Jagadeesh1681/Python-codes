#Sum of first n natural numbers.
n=int(input("Enter a num :"))
sum=0
for i in range(1,n+1):
	sum=sum+i
print("The sum of first {} natural numbers = {}".format(n,sum))
