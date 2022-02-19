
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def printList(self):
        while(self.head):
            print(self.head.data)
            self.head = self.head.next
        


linkedlist = LinkedList()
linkedlist.head = Node(1)
secodn_value = Node(2)
third_value = Node(1)

linkedlist.head.next = secodn_value
secodn_value.next = third_value

linkedlist.tail = third_value
# linkedlist.tail = linkedlist.head

linkedlist.printList()

    
