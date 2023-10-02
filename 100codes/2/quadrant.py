#Quadrant.py
x=int(input("Enter val of x :"))
y=int(input("Enter val of y :"))
if (x>0 and y>0):
	print("point({} , {}) lies in First Quadrant".format(x,y))
elif (x<0 and y>0):
	print("point({} , {}) lies in Second Quadrant".format(x,y))
elif (x<0 and y<0):
	print("point({} , {}) lies in Third Quadrant".format(x,y))
elif (x>0 and y<0):
	print("point({} , {}) lies in Fourth Quadrant".format(x,y))
elif (x!=0 and y==0):
	print("point({} , {}) lies in X-axis".format(x,y))
elif (x==0 and y!=0):
	print("point({} , {}) lies in Y-axis".format(x,y))
else :
	print("point({} , {}) lies in Origin".format(x,y))
	
