# height: Number of edges in longest path from the node to a leaf node.
# So,
#              height of a tree = height of root node
#              height of a tree with 1 node = 0
# depth:
# depth is no of edges in path from root to that node
#           depth of root node = 0

class Node:
    def __init__(self, data) -> None:
        self.data  = data
        self.left  = None
        self.right = None

    def buildTree(self, data):
        if self.data == data:
            return 

        elif data < self.data:
            if self.left:
                self.left.buildTree(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.buildTree(data)

            else:
                self.right = Node(data)

    def findHeight(self,root):
        if root == None:
            return -1        
        

        return max(self.findHeight(root.left), self.findHeight(root.right)) + 1


s = Node(4)
s.buildTree(2)
s.buildTree(1)
s.buildTree(3)
s.buildTree(6)
s.buildTree(5)
print(s.findHeight(s))


        