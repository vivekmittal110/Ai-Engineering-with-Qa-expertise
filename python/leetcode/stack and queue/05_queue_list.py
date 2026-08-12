class Queue:
    def __init__(self):
        self.que = []
        self.size = 0
    def push(self,x):
        self.size +=1
        self.que.append(x)
    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        x = self.que[0]
        del self.que[0]
        return x

    def peek(self):
        if self.size == 0:
            return None
        return self.que[0]

    def lenght(self):
        return self.size

    def isEmpty(self):
        return True if self.size == 0 else False


s1 = Queue()
s1.push(9)
s1.push(94)
s1.push(96)
print(s1.pop())
print(s1.peek())
print(s1.lenght())
print(s1.isEmpty())