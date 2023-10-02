n=int(input("Enter no.of chocolates in the jar :"))
list1,list2=[],[]
for i in range(n):
	a=int(input("Enter a number :"))
	list1.append(a)
print(list1)
b=list1.count(0)
for j in list1:
	if j == 0:
		list2.append(j)
print(list2)
for k in list2:
	for l in list1:
		if l == k:
			list1.remove(k)
list1.extend(list2)
print(list1)

	