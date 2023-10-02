def swap(new_list):
	if pos1>=0 and pos2<=len(new_list):
		new_list[pos1],new_list[pos2]=new_list[pos2],new_list[pos1]
		return new_list

#main program
pos1=int(input("Enter a number : "))
pos2=int(input("Enter a number :"))
l=[1,2,3,4,5,6,7,8,9,10]
print(swap(l))