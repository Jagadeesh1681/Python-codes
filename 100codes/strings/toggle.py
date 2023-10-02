n=input("Enter a string :")
s=str()
for i in n:
	if i.isupper():
		i=i.lower()
		s=s+i
	else:
		i=i.upper()
		s=s+i
print(n,"after toggling",s)
