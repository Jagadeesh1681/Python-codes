#program for finding max. no .of handshakes.
n=int(input("Enter no.of people :"))
sum=0
for i in range(n-1,0,-1):
	sum=sum+i
print("The maximum no.of handshakes = {}".format(sum))
