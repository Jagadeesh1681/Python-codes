n=input("Enter a string :")
result=""
a=['(',')','[',']','{','}']
for i in n:
	if i not in a:
		result+=i
print(result)
