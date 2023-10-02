#leap year or not.py
n=int(input("Enter a year :"))
if(n%400==0) or(n%100!=0) and (n%4==0) :
	print("{} is a Leap year".format(n))
else:
	print("{} is not a Leap year".format(n))
		
