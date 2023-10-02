s=input("Enter a sentence : ")
count=1
for word in s:
	if chr(ord(word)) == ' ':
		count+=1
print(count)