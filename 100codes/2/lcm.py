#lowest common multiple.py
a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
for i in range(max(a,b),(a*b)+1):
	if (i%a==0) and (i%b==0):
	    lcm=i
	    break
print("LCM of {} , {} = {}".format(a,b,lcm))
