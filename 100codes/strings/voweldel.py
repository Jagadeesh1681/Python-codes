#program to remove vowels in a given string
n=input("Enter a string :")
n=n.lower()
result=""
b=['a','e','i','o','u']
for i in n:
    if i not in b:
        result=result+i
print(result)
        
