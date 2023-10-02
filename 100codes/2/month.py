#month.py
n=int(input("enter month (number) :"))
year=int(input("Enter year" :))
if (n==2):
	if (year%100!=0) and (year%4==0) or (year%400==0):
		print("Number of days =",29)
	else:
		print("Number of days =",28)
elif (n == 1 or 3 or 5 or 7 or 9 or 11):
	print("Number of days =",31)
else:
	print("Number of days =",30)
