print ("please type your the day of your birth")
a=int(input())
print ("please type your the month of your birth")
b=int(input())
print ("please type your the year of your birth")
c=int(input())

print ("please type today's date")
x=int(input())
print ("please type the month")
y=int(input())
print ("please type the year")
z=int(input())

d=z-c
e=y-b
f=x-a

if (e>=0 and f>=0):
    print("integer yeas",d)
else:
    print("integer years",d-1)
if d>=18:
    print("you are allowed to buy alchogol")
else:
    print("unfortunatelly, not today")