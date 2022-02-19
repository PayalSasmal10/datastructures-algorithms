class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class reverseLinkedlist:
    def __init__(self) -> None:
        self.head = None

    def reverselist(self):
        prv = None
        current = self.head
        next = None
        while(current is not None):
            next = current.next
            current.next = prv
            prv = current 
            current = next
        self.head = prv
    
    def printList(self):
        while(self.head):
            print(self.head.data)
            self.head = self.head.next


reverselinkedlist = reverseLinkedlist()
reverselinkedlist.head = Node(3)
second_value = Node(7)
thrird_value = Node(9)

reverselinkedlist.head.next = second_value
second_value.next = thrird_value

#reverselinkedlist.printList()
reverselinkedlist.reverselist()
reverselinkedlist.printList()