s1,s2=input("Enter first string : "),input("Enter second string : ")
result_str=[ch for ch in s1 if ch not in s2]
for val in result_str:
	print(val,end="")