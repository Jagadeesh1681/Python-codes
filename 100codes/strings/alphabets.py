n=input("Enter a string :")
result=""
for i in range(len(n)):
	if (65<=ord(n[i])<=90 or 97<=ord(n[i])<=122):
		result=result+n[i]
print(result)
