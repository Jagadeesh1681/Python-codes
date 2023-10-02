def flat_list(list):
	new_list=[]
	for i in range(len(list)+1):
		new_list.append(i)
	return new_list
l=[1,2,3,4,5,[6,7,8,9,10],11,12,13,14,15]
print(flat_list(l))
	