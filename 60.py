class Deque:
    def __init__(self):
        self._list = []

    def push_front(self, element):
        self._list.insert(0, element)
        print('ok')

    def push_back(self, element):
        self._list.append(element)
        print('ok')

    def pop_front(self):
        b = self._list.pop(0)
        print(b)

    def pop_back(self):
        c = self._list.pop()
        print(c)

    def front(self):
        print(self._list[0])

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


deque=Deque()


while True:
    a = input().split()
    if a[0] == 'front':
        deque.front()
    if a[0] == 'back':
        deque.back()
    elif a[0] == 'pop_front':
        deque.pop_front()
    elif a[0] == 'pop_back':
        deque.pop_back()
    elif a[0] == 'push_front':
        deque.push_front(int(a[1]))
    elif a[0] == 'push_back':
        deque.push_back(int(a[1]))
    elif a[0] == 'size':
        deque.size()
    elif a[0] == 'clear':
        deque.clear()
    elif a[0] == 'exit':
        deque.exit()