#digitsum.py
n=input("Enter a number :")
sum=0
for i in range(len(n)):
	sum=sum+int(n[i])
print("{} is the sum of the digits of the number {}".format(sum,n))
	

