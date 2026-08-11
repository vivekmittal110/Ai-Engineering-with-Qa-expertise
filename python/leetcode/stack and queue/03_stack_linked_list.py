class ListNode:
    def __init__(self,data):
        self.val = data
        self.next = None
        

class Stack:
    def __init__(self):
        self.top = None
        self.s = 0
    def push(self,x):
        self.s+=1
        if self.top is None:
            self.top = ListNode(x)
            return
        else:
            newNode = ListNode(x)
            newNode.next = self.top
            self.top = newNode
            return
    def pop(self):
        if self.top is None:
            return None
        self.s-=1
        x = self.top.val
        self.top = self.top.next
        return x
    def peek(self):
        if self.top is None:
            return None
        return self.top.val
    def size(self):
        return self.s

s1 = Stack()
s1.push(3)
s1.push(2)
s1.push(4)
s1.push(5)
s1.pop()
s1.pop()
print(s1.peek())
print(s1.size())