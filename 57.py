class Queue:
    def __init__(self):
        self._list=[]

    def push(self,n):
        self._list.append(n)
        print('ok')

    def pop(self):
        b=self._list.pop(0)
        print(b)

    def front(self):
        print(self._list[0])

    def size(self):
        print(len(self._list))

    def clear(self):
        self._list.clear()
        print('ok')

    def exit(self):
        print('bye')
        exit()

queue=Queue()
while True:
    a = input().split()
    if a[0] == 'front':
        queue.front()
    elif a[0] == 'pop':
        queue.pop()
    elif a[0] == 'push':
        queue.push(int(a[1]))
    elif a[0] == 'size':
        queue.size()
    elif a[0] == 'clear':
        queue.clear()
    elif a[0] == 'exit':
        queue.exit()