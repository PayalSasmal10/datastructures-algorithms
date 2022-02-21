
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class SingleLinkedlist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # add_front with tail
    def add_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    # add_back with tail
    def add_back(self, data):
        if (self.head == None):
            new_node = Node(data)
            self.head = self.tail = new_node
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node


    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, " -> ", end="")
            temp = temp.next
        print("end")
    

s = SingleLinkedlist()
# s.add_front(1)
# s.add_front(5)
# s.add_front(2)
# s.printList()

s.add_back(10)
s.add_back(22)
s.add_back(23)
s.printList()