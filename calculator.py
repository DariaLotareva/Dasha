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


def read():
    t=open('calculator.txt', mode='rt')
    lines = t.readlines()
    t.close()
    print(lines)
    return t

read()


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
        lines = [x1, '+', y1, '=', d1, '\n']
        f.writelines(lines)

    elif op == '-':
        y = float(input())
        d = x - y
        print(d)
        d1 = str(d)
        x1=str(x)
        y1=str(y)
        lines = [x1, '-', y1, '=', d1, '\n']
        f.writelines(lines)

    elif op == '*':
        y = float(input())
        d = x * y
        print(d)
        d1 = str(d)
        x1=str(x)
        y1=str(y)
        lines=[x1,'*',y1,'=',d1,'\n']
        f.writelines(lines)


    elif op == '/':
        y = float(input())
        d = x / y
        print(d)
        d1 = str(d)
        x1=str(x)
        y1=str(y)
        lines = [x1, '/', y1, '=', d1, '\n']
        f.writelines(lines)

    elif op == '**':
        y = float(input())
        d = x ** y
        print(d)
        d1 = str(d)
        x1=str(x)
        y1=str(y)
        lines = [x1, '**', y1, '=', d1, '\n']
        f.writelines(lines)

