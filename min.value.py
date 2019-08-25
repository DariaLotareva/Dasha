print("1st value")
a=float(input())
print("2nd value")
b=float(input())
print("3rd value")
c=float(input())
print("4th value")
d=float(input())
print("5th value")
e=float(input())

if (a<=b and a<=c and a<=d and a<=e):
    print("min value is",a)
elif (b<=a and b<=c and b<=d and b<=e):
    print("min value is", b)
elif(c<=a and c<=b and c<=d and c<=e):
    print("min value is", c)
elif (d<=a and d<=c and d<=b and d<=e):
    print("min value is", d)
else:
    print("min value is", e)