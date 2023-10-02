str=input("Enter a string : ")
temp,sum="0",0
for ch in str:
	if ch.isdigit():
		temp+=ch
	else:
		sum+=int(temp)
		temp="0"
print(sum)