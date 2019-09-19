class Stack:
    def __init__(self):
        self._list=[]

    def push(self,n):
        self._list.append(n)
        print('ok')

    def pop(self):
        b=self._list.pop()
        print(b)


    def back(self):
        print(self._list[-1])

    def size(self):
        print(len(self._list))

    def clear(self):
        self._list.clear()
        print('ok')

    def exit(self):
        print('bye')
        exit()

stack=Stack()

while True:
    a = input().split()
    if a[0] == 'back':
        stack.back()
    elif a[0] == 'pop':
        stack.pop()
    elif a[0] == 'push':
        stack.push(int(a[1]))
    elif a[0] == 'size':
        stack.size()
    elif a[0] == 'clear':
        stack.clear()
    elif a[0] == 'exit':
        stack.exit()


