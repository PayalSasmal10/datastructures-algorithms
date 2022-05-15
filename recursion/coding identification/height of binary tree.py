
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def buildTree(self, data):
        if self.data == data:
            return

        # if data is less than self.data then add to left
        if self.data > data:
            if self.left is not None:
                self.left.buildTree(data)
            else:
                self.left = Node(data)
        
        # if data is less than self.data then add to right
        elif self.data < data:
            if self.right is not None:
                self.right.buildTree(data)
            else:
                self.right = Node(data)

        
    def preorder(self,root):
        if root:
            print(root.data, "->", end="")
            self.preorder(root.left)
            self.preorder(root.right)
    def height(self, root):
        
        if root == None:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        print("data :", root.data)
        print("lh:", lh)
        print("rh:", rh)

        return 1+max(lh,rh)



s = Node(4)
s.buildTree(3)
#print(s.buildTree(3))
s.buildTree(1)
s.buildTree(4)
s.buildTree(5)
s.buildTree(6)
s.buildTree(7)
s.preorder(s)
print("end")

print(s.height(s))
