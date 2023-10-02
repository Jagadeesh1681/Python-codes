s=input("Enter a string : ")
result_str=''
for i in range(len(s)):
	result_str+=chr(ord(s[i])+1)
print(result_str)
	