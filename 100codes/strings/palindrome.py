#palindrome
n=input("Enter a string :")
n=n.lower()
a=n[::-1]
if (a==n):
	print("{} is palindrome".format(n))
else:
	print("{} is not palindrome".format(n))
