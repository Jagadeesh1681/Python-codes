#addition of fractions.
x1,y1=int(input("enter numerator x1 :")),int(input("enter denominator y1 :"))
x2,y2=int(input("enter numerator x2 :")),int(input("enter denominator y2 :"))
for i in range(1,min(y1,y2)+1):
	if (y1%i==0 and y2%i==0):
		hcf=i
lcm=int((y1*y2)/hcf)
x,y=(x1/y1)*lcm,(x2/y2)*lcm
num=int(x+y)
print("The fractional addition = {}/{}".format(num,lcm))
