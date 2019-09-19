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


def show_history():
    t=open('calculator.txt', mode='rt')
    lines = t.readlines()
    t.close()
    print(lines)
    return t

def exit():
    print('bye')
    exit()


print('please text (count), (show_history) or (exit)')
while True:
    a = input().split()
    f = open('calculator.txt', mode='at')
    if a[0]=='show_history':
        show_history()
    if a[0] == 'exit':
        exit()
    if a[0]=='count':
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

