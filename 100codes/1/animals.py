#Program for finding no.of animals with 4 legs and 2 legs.
h=int(input("Enter total no.of heads in the group :"))
l=int(input("Enter total no.of feet in the group :"))
x=(l-2*h)/2
y=h-x
print("Total no.of animals with four feet = {}".format(x))
print("Total no.of animals with two feet = {}".format(y))
