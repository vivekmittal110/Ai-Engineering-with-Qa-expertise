
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0
    def push(self,x):
        self.size += 1
        self.queue.append(x)
    def pop(self):
        if self.size==0:
            return
        x = self.queue.pop(0)
        # self.queue.pop(0)
        self.size -= 1
        return x
    def get_size(self):
        return self.size
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        ans = []
        if root == None:
            return ans
        
        queue = Queue()
        queue.push(root)
        ans.append([root.val])
        
        while queue.get_size()>0:
            l = queue.get_size()
            level = []
            for i in range(l):
                front = queue.pop()
                if front.left != None:
                    queue.push(front.left)
                    level.append(front.left.val)
                if front.right != None:
                    queue.push(front.right)
                    level.append(front.right.val)
            if len(level)>0:
                ans.append(level)
        return ans[::-1]

                