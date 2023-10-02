#program to find no.of vowels in a given string.
n=input("Enter a string :")
n=n.lower()
a=['a','e','i','o','u']
x=0
for i in range(len(n)):
	for j in a:
		if (j == n[i]):
			x=x+1
print("No.of vowels in {} = {}".format(n,x))
			
