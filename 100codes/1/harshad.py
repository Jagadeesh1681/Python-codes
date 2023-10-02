#harshad number.py
n=int(input("Enter a number :"))
a=str(n)
sum=0
for i in range(len(a)):
		sum=sum + int(a[i])
if (n%sum == 0):
    print("{} is a Harshad number".format(n))
else:
    print("{} is not a Harshad number".format(n))
