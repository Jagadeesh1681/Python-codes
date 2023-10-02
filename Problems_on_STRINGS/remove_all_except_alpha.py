s=input("Enter a string : ")
result_str=''
for ch in s:
	if (ord(ch)>=65 and ord(ch)<=90) or (ord(ch)>=97 and ord(ch)<=122):
		result_str+=ch
print(result_str)