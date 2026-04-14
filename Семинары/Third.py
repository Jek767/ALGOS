#Задание 1
"""class Stack:
    def __init__(self):
        self.item = []

    def push(self,num):
        self.item.append(num)

    def pop(self):
        return self.item.pop()

    def size(self):
        return len(self.item)

    def I_see_you(self):
        return self.item

    def peek(self):
        return self.item[-1]

class Queue:
    def __init__(self):
        self.main_stack = Stack()
        self.dop_stack = Stack()

    def enqueue(self,num):
        self.main_stack.push(num)

    def dequeue(self):
        if self.dop_stack.size()==0:
            for i in range(0, self.main_stack.size()):
                self.dop_stack.push(self.main_stack.pop())

        return self.dop_stack.pop()

    def print(self):
        print(self.dop_stack.I_see_you())

    def peek(self):
        if self.dop_stack.size() == 0:
            for i in range(0, self.main_stack.size()):
                self.dop_stack.push(self.main_stack.pop())

        return self.dop_stack.peek()

q = Queue()
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)"""
#Задание 2
"""Я просеиваю очередь двумя циклами каждый раз когда мне нужен доступ к верхнему элементу(тому который только что положили)"""
from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
def antiQ(q: Queue) -> str:

    tempQ = Queue()
    size = q.size()
    temp = 0

    for i in range(0,size):

        if i == size-1:
            temp = q.peek()

        tempQ.enqueue(q.dequeue())

    for i in range(0,tempQ.size()):
        q.enqueue(tempQ.dequeue())

    return temp
def antiQ_del(q: Queue) -> str:

    tempQ = Queue()
    size = q.size()
    temp = 0

    for i in range(0,size):
        if i == size-1:
            temp = q.dequeue()
        else:
            tempQ.enqueue(q.dequeue())

    for i in range(0,tempQ.size()):
        q.enqueue(tempQ.dequeue())
def correct(staples: str) -> bool:

    matching = {')': '(', ']': '[', '}': '{'}
    q = Queue()

    for i in staples:
        if i in"([{":
            q.enqueue(i)
        else:
            if antiQ(q) != matching[i]:
                return False
            antiQ_del(q)

    return q.size() == 0
tests = ["([]){}", "([)]", "((()))", ")(", ""]
"""for t in tests:
    print(correct(t))"""
#3.1
class Stack:
    def __init__(self):
        self.item = []

    def push(self, num):
        self.item.append(num)

    def pop(self):
        return self.item.pop()

    def size(self):
        return len(self.item)

    def I_see_you(self):
        return self.item

    def peek(self):
        return self.item[-1]
class MyQueue:
    def __init__(self):
        self.main_stack = Stack()
        self.dop_stack = Stack()

    def push(self, num):
        self.main_stack.push(num)

    def pop(self):
        if self.dop_stack.size() == 0:
            for i in range(0, self.main_stack.size()):
                self.dop_stack.push(self.main_stack.pop())

        return self.dop_stack.pop()

    def peek(self):
        if self.dop_stack.size() == 0:
            for i in range(0, self.main_stack.size()):
                self.dop_stack.push(self.main_stack.pop())

        return self.dop_stack.peek()

    def empty(self):
        return self.main_stack.size() == 0 and self.dop_stack.size() == 0
#Задание 3.2
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.first = 0
        self.last = -1
        self.queue = [None]*k

    def enQueue(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        self.last = (self.last + 1) % self.max_size
        self.queue[self.last] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.queue[self.first] = None
        self.first = (self.first + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.first]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.last]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size
"""myCircularQueue = MyCircularQueue(3)
myCircularQueue.enQueue(1) #// возвращает True
myCircularQueue.enQueue(2) #// возвращает True
myCircularQueue.enQueue(3)# // возвращает True
myCircularQueue.enQueue(4) #// возвращает False
myCircularQueue.Rear() #// возвращает 3
myCircularQueue.isFull() #// возвращает True
myCircularQueue.deQueue() #// возвращает True
myCircularQueue.enQueue(4) #// возвращает True
myCircularQueue.Rear() #// возвращает 4"""
#Задание 3.8
from collections import deque
def predictPartyVictory(senate: str) -> str:

    n = len(senate)
    Radiant = deque()
    Dire = deque()

    for i in range(n):
        if senate[i] == 'R':
            Radiant.append(i)
        else:
            Dire.append(i)

    while Radiant and Dire:
        r_num = Radiant.popleft()
        d_num = Dire.popleft()

        if r_num < d_num:
            Radiant.append(r_num + n)
        else:
            Dire.append(d_num + n)
            
    return "Radiant" if Radiant else "Dire"
s = "RRRDDDDDR"
#print(predictPartyVictory(s))
#Задание 4
"""import heapq
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def enqueue(self, priority, dish):
        heapq.heappush(self.heap, (-priority, dish))

    def dequeue(self):
        if not self.heap:
            raise IndexError("Очередь пуста")
        return heapq.heappop(self.heap)[1]

    def is_empty(self):
        return len(self.heap) == 0
pq = PriorityQueue()
pq.enqueue(1,"Обычная заявка")
pq.enqueue( 10,"Срочная заявка")
pq.enqueue( 100,"Критическая заявка")
pq.enqueue( 1000,"Заявка на 'Попить чай'")
while not pq.is_empty():
    print(pq.dequeue())"""

from collections import deque
class PQ:
    def __init__(self,prior_list):
        self.item = {}
        self.prior_list = prior_list
        for i in prior_list:
            self.item[i] = []

    def push(self,priority,dish):
        self.item[priority].append(dish)

    def pop(self):
        for i in self.prior_list:
            if len(self.item[i])!=0:
                return self.item[i].pop(0)


pq = PQ([1,10,100,1000,10000])
pq.push( 1,"Обычная заявка")
pq.push( 10,"Обычная заявка")
pq.push( 100,"Обычная заявка")
pq.push( 10000,"Chjxyfz pfzdrf")
pq.push( 100,"Обычная заявка2")
pq.push( 100,"Обычная заявка3")
pq.push( 100,"Обычная заявка4")
pq.push( 100,"Обычная заявка5")
pq.pop()
pq.pop()
pq.pop()


print(pq.item)


