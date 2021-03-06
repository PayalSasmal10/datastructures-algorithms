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
        while(current is not None):
            temp = current.next
            current.next = prv
            prv = current 
            current = temp
        self.head = prv
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, " -> ", end="")
            temp = temp.next
        print("end")


reverselinkedlist = reverseLinkedlist()
reverselinkedlist.head = Node(3)
second_value = Node(7)
thrird_value = Node(9)

reverselinkedlist.head.next = second_value
second_value.next = thrird_value

#reverselinkedlist.printList()
reverselinkedlist.reverselist()
reverselinkedlist.printList()