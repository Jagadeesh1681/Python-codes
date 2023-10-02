s=input("Enter a sentence : ")
result_str=''
for i in range(len(s)):
	if (ord(s[i])>=65 and ord(s[i])<=90):
		result_str+=chr(ord(s[i])+32)
	else:
		result_str+=chr(ord(s[i])-32)
print(result_str)
		