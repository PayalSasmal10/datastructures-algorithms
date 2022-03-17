
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
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
    # 1st way to fetch the data

    # def findMin(self,root):
    #     if root:
    #         if root.left == None:
    #             print(root.data)
    #         self.findMin(root.left)

    # def findMax(self, root):
    #     if root:
    #         if root.right == None:
    #             print(root.data)
    #         self.findMax(root.right)
    
    # 2nd way
    def findMin(root):
        current_node = root
        
        while(current_node.left != None):
            current_node = current_node.left
        print(current_node.data)

    def findMax(root):
        current_node = root

        while(current_node.right != None):
            current_node = current_node.right
        print(current_node.data)


s = Node(4)
s.buildTree(2)
s.buildTree(1)
s.buildTree(3)
s.buildTree(6)
s.buildTree(5)
# for 1st way
#s.findMin(s)
#s.findMax(s)

s.findMin()
s.findMax()

