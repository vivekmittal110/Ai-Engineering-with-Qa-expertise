class ListNode:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None

root = ListNode(1)
root.left = ListNode(2)
root.right = ListNode(3)
print(root.left.val)
print(root.val)
root.left.right = ListNode(4)
print(root.left.right.val)