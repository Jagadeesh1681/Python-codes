n=int(input("Enter a number :"))
a=str(n)
even,odd=0,0
for i in range(len(a)):
	if (int(a[i]) % 2 == 0):
		even+=int(a[i])
	else:
		odd+=int(a[i])
diff=even-odd
if (diff <0):
	diff=diff*(-1)
print("difference :",diff)
		
