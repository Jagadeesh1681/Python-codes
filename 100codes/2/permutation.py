#program for N people to occupy r seats.
n=int(input("Enter no.of people :"))
r=int(input("Enter no.of seats available :"))
fact1,fact2=1,1
for i in range(1,n+1):
	fact1=fact1*i
for j in range(1,(n-r+1)):
	fact2=fact2*j
permutation=fact1//fact2
print("{} people can occupy {} seats in {} ways".format(n,r,permutation))
	
