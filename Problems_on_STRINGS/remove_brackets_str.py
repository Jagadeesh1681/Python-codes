s=input("Enter a mathematical expression : ")
result_str=''
for ch in s:
	if(ord(ch) != 40 and ord(ch) != 41):
		result_str+=ch
print(result_str)