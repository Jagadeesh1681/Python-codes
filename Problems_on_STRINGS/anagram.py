s1,s2=input("Enter first string :"),input("Enter second string :")
x=0
if (len(s1) == len(s2)):
	for i in s1:
		for j in s2:
			if i ==j:
				x+=1
	if x == len(s1):
		print("{} and {} are ANAGRAMS".format(s1,s2))
else:
	print("{} and {} are not ANAGRAMS".format(s1,s2))
				
	
				