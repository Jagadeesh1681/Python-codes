#roots for quadratic equation.
import math
a=float(input("Enter co-efficient of x square :"))
b=float(input("Enter co-efficient of x  :"))
c=float(input("Enter constant value :"))
d=(b**2)-(4*a*c)
e=math.sqrt(d)
if (d == 0):
	x=(-b)/(2*a)
	y=x
	print("Equal and real roots : {} , {}".format(x,y))
elif (d>0):
	x=(-b+e)/(2*a)
	y=(-b-e)/(2*a)
	print("real roots : {} , {}".format(x,y))
else :
	x=(-b+e)/(2*a)
	y=(-b-e)/(2*a)
	print("Imaginary roots : {} i , {} i".format(x,y))

	

