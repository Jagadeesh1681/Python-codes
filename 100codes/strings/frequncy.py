s=input("Enter a string : ")
count_list=[]
for i in s:
	count=0
	for j in s:
		if i == j:
			count+=1
break
	count_list.append(count)
print(count_list)