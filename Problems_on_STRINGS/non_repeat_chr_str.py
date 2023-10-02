s=input("Enter a string :")
result=[ch for ch in s if s.count(ch) == 1]
for x in result:
	print(x,end=",")