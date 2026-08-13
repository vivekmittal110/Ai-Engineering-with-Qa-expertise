class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0

    def push(self,x):
        self.lenght+=1
        if self.head==None:
            self.head = ListNode(x)
            self.tail = self.head
        else:
            self.tail.next = ListNode(x)
            self.tail = self.tail.next

    def pop(self):
        if self.head==None:
            return None
        else:
            self.lenght-=1
            x = self.head.val
            self.head = self.head.next
            return x
    def size(self):
        return self.lenght

    def peek(self):
        if self.head == None:
            return None
        return self.head.val

    def isEmpty(self):
        return True if self.head == None else False

q = Queue()
q.push(3)
q.push(4)
q.push(5)
q.push(6)
print(q.pop())
print(q.peek())
print(q.isEmpty())
print(q.size())