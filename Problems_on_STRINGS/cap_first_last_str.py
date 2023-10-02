s=input("Enter a string : ")
result_str=''
for ch in range(len(s)):
	if(ord(s[ch]>=97)) and (ord(s[ch]<=122)):
		s[ch] = chr(ord(s[ch]-32))
	else:
		s[ch] = s[ch]
	if (ord(s[ch-1]) >=90) and (ord(s[ch-1]) <=122):
		s[ch-1] = chr(ord(s[ch-1]-32))
	else:
		s[ch-1] = s[ch-1]
	result=''.join(s)
print(result)
	