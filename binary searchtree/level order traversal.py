# Binary first Traversal
import queue



class Node:
    def __init__(self, data) -> None:
       self.data = data
       self.left = None
       self.right = None
    
    def buildTree(self,data):
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

    def levelOrder(root):
        if root == None:
            return
        queue = []
        queue.append(root)
        while(len(queue)>0):
            print(queue[0].data)
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


s = Node(10)
s.buildTree(8)
s.buildTree(5)
s.buildTree(6)
s.buildTree(15)
s.buildTree(11)
s.buildTree(12)
s.buildTree(13)
s.levelOrder()

"""

            ‌10‌ ‌
           ‌/‌  ‌\‌ ‌
         ‌8     ‌15 ‌ ‌
        ‌/‌  ‌\‌   /  
       ‌5‌   ‌ 6  11
                 \
                 12
                  \
                   13  
"""
