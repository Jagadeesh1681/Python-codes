#digit count
n=int(input("Enter a number :"))
a=n
digit=0
while(n!=0):
	n=n//10
	digit=digit+1
print("No.of digits in {} ={}".format(a,digit))
	
	
