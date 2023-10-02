n=input("Enter a aplhabetical string : ")
vowels=['a','e','i','o','u']
vcount,ccount=0,0
for i in n:
	for j in vowels:
		if i == j:
			vcount+=1
			break
	else:
		ccount+=1
print("Vowel count = ",vcount)
print("Consonant count = ",ccount)
		
