#perfect squares.py
import math
n=int(input("Enter a number :"))
a=math.sqrt(n)
if (a*a == n):
	print("{} is a perfect square".format(n))
else:
	print("{} is not a perfect square".format(n))
