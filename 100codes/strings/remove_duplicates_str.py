s=input("Enter a string :")
result_str=''
for ch in s:
	if s.count(ch)<=1:
		result_str+=ch
print(result_str)