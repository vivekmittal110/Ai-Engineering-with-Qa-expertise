class Stack:
    def __init__(self):
        self.st=[]
    def push(self,x):
        self.st.append(x)

    def pop(self):
        if len(self.st)==0:
            return -1
        x = self.st[-1]
        self.st.pop()
        return x
    
    def peek(self):
        if len(self.st)==0:
            return None
        return self.st[-1]

    def isEmpty(self):
        if len(self.st)==0:
            return True
        else:
            return False
    def size(self):
        return len(self.st) 

s1 = Stack()
s1.push(9)
s1.push(94)
s1.push(96)
s1.pop()
s1.pop()
print(s1.peek())
print(s1.size())
print(s1.isEmpty())