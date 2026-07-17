class twod:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def show(self):
        print("i = ", self.i)
        print("j = ", self.j)
class threed(twod):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print("i = ", self.i)
        print("j = ", self.j)
        print("k = ", self.k)
a = twod(7,5)
b = threed(7,5,3)
a.show()
b.show()