num=[1,2,3,4,5,6,7,8,9,10]
even=[i for i in num if i%2==0]
odd=[i for i in num if i%2!=0]
print("Even numbers = {}".format(even))
print("Odd numbers = {}".format(odd))