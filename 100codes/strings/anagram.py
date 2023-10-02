a=input("Enter first string :")
b=input("Enter second string :")
x=0
if (len(a) == len(b)):
	for i in a:
		for j in b:
			if (i == j):
				x=x+1
if (x == len(a)):
	print("{} and {} are ANAGRAMS".format(a,b))
else:
	print("{} and {} are not ANAGRAMS".format(a,b))
