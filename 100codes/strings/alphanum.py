n=input("Enter a alpha-numeric string :")
sum=0
a=['0','1','2','3','4','5','6','7','8','9']
for i in n:
	for j in range(len(a)):
		if i == a[j]:
			sum+=int(i)
print(sum)
		
	
