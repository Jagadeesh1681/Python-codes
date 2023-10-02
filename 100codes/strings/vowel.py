#program to check whether given alphabet is vowel or consonant.
x=input("Enter any alphabet :")
x=x.lower()
a=['a','e','i','o','u']
for i in a:
    if x == i:
        print("{} is a vowel".format(x))
        break
    else:
        print("{} is a consonant".format(x))
    break
