#program to check whether given character is an alphabet or not.
x=input("Enter any character :")
y=ord(x)
if (65<=y<=90 or 97<=y<=122):
	print("{} is an alphabet".format(x))
else:
	print("{} is not an alphabet".format(x))

