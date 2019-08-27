print('please type the speed')
v=int(input())
print('please type the time')
t=int(input())
s=abs(v)*t
if v>=0:
    print('the km of the road is',s%109)
else:
    print('the km of the road is',(109-(s%109)))