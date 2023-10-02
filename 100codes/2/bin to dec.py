# bin to dec.py
n=input("Enter binary number :")
dec=0
for i in range(len(n)):
	if (n[i] == 0 or 1):
		dec=dec+(2**(i+1))*int(n[i])
print(dec)
		
