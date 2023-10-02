#palindrome.py
n=input("Enter a number :")
if (n == n[::-1]):
	print("{} is a Palindrome".format(n))
else:
	print("{} is not a Palindrome".format(n))
