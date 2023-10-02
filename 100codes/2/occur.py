#occurence.py
n=input("Enter a number :")
d=input("Enter a digit :")
count=0
for i in range(len(n)):
    if(n[i] == d):
        count+=1
print("The digit {} has occured {} times in {}".format(d,count,n))
