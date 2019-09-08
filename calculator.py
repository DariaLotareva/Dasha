#
# def sum(a,b):
#     c=a+b(a,b)
#
#     return c
#
# def dim(a,b):
#     c=a-b(a,b)
#
#     return c
# def mul(a,b):
#     c=a*b(a,b)
#     return c
# def div(a,b):
#     c=a/b(a,b)
#     return c
# def exp(a,b):
#     c=a**b(a,b)
#     return c
#
# while True:
#   a=float(input())
# s=(input())
# if s=='+':
#        b=float(input())
#        print(sum())





while True:
    f = open('calculator.txt', mode='at')
    x = float(input())
    op = input()
    if op == '+':
        y = float(input())
        d=x+y
        print(d)
        d1 = str(d)
        x1=str(x)
        y1=str(y)
        f.write(x1)
        f.write('+')
        f.write(y1)
        f.write('=')
        f.write(d1)
        f.write('\n')

    elif op == '-':
        y = float(input())
        d = x - y
        print(d)
        d1 = str(d)
        x1=str(x)
        y1=str(y)
        f.write(x1)
        f.write('-')
        f.write(y1)
        f.write('=')
        f.write(d1)
        f.write('\n')

    elif op == '*':
        y = float(input())
        d = x * y
        print(d)
        d1 = str(d)
        x1=str(x)
        y1=str(y)
        f.write(x1)
        f.write('*')
        f.write(y1)
        f.write('=')
        f.write(d1)
        f.write('\n')

    elif op == '/':
        y = float(input())
        d = x / y
        print(d)
        d1 = str(d)
        x1=str(x)
        y1=str(y)
        f.write(x1)
        f.write('/')
        f.write(y1)
        f.write('=')
        f.write(d1)
        f.write('\n')

    elif op == '**':
        y = float(input())
        d = x ** y
        print(d)
        d1 = str(d)
        x1=str(x)
        y1=str(y)
        f.write(x1)
        f.write('**')
        f.write(y1)
        f.write('=')
        f.write(d1)
        f.write('\n')

