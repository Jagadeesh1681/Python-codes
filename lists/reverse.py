def reverse(list):
	new_list=[]
	for i in range(1,len(list)+1):
		new_list.append(list[-i])
	return new_list
l=[1,2,3,4,5,6,7,8,9,10]
print(reverse(l))
		