n=int(input("How many numbers :"))
odd,even=0,0
for i in range(1,n+1):
	a=int(input("Enter {} number :".format(i)))
	if (a%2 == 0):
		even+=a
	else:
		odd+=a
diff=even-odd
if (diff <0):
	diff=diff*(-1)
print(diff)

	
		
