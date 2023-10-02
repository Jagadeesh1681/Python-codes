l=[]
largest=0
n=int(input("Enter lenght of LIST :"))
#Adding values into the list
for j in range(n):
	a=int(input("Enter a number :"))
	l.append(a)
#Finding the largest integer in the list
for i in l:
	for j in range(len(l)):
		if i > l[j]:
			largest = i
print("largest = ",i)

	