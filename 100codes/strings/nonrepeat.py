n=input("Enter a string :")
count=0
for i in n:
    for j in n:
        if i == j:
            count+=1
        if count >1:
            break
    if count == 1:
        print(i,end=" ")
        count=0
