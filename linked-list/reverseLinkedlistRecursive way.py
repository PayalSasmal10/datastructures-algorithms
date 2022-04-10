class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class reverseLinkedlist:
    def __init__(self) -> None:
        self.head = None

    def add_front(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode

        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def reverselist(self, head): 
        if head == None or head.next == None:
            print("inside")
            return head
        
        newHead = self.reverselist(head.next)
        headNext = head.next
        headNext.next = head
        head.next = None
        return newHead
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, " -> ", end="")
            temp = temp.next
        print("end")


reverselinkedlist = reverseLinkedlist()
reverselinkedlist.add_front(4)
reverselinkedlist.add_front(2)
reverselinkedlist.add_front(14)
reverselinkedlist.add_front(48)
reverselinkedlist.printList()
reverselinkedlist.head = reverselinkedlist.reverselist(reverselinkedlist.head)
reverselinkedlist.printList()

