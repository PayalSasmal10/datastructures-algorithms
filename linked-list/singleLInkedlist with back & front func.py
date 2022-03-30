
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None

    # add_front without tail 
    def add_front(self,data):
        if (self.head == None):
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    
    def add_back(self, data):
        if (self.head == None):
            new_node = Node(data)
            self.head = new_node
        else:
                        
            tmp = self.head
            
            while(tmp):
                print(tmp)
                new_node = Node(data)
                if tmp.next == None:
                    tmp.next = new_node
                    new_node.next = None
                    tmp = tmp.next

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, "->", end="")
            temp = temp.next
        print("end")



slinkedlist = SingleLinkedList()
# slinkedlist.add_front(3)
# slinkedlist.add_front(7)
# slinkedlist.add_front(30)
# slinkedlist.printList()

slinkedlist.add_back(3)
slinkedlist.add_back(7)
slinkedlist.add_back(30)
slinkedlist.printList()
