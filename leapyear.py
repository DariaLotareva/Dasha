print('please write the year')
a=int(input())
if ((a%4==0) and (a%100!=0)):
    print('yes')
else:
    print('no')