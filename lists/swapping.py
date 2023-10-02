def swap(new_list):
	new_list[0],new_list[-1]=new_list[-1],new_list[0]
	return new_list
#main program
l=[1,2,3,4,5,6]
print(swap(l))