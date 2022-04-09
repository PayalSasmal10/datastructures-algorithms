class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class reverseLinkedlist:
    def __init__(self) -> None:
        self.head = None

    def reverselist(self, head): 
        if head == None or head.next == None:
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
reverselinkedlist.head = Node(3)
second_value = Node(7)
thrird_value = Node(9)

reverselinkedlist.head.next = second_value
second_value.next = thrird_value

#reverselinkedlist.printList()
reverselinkedlist.reverselist(reverselinkedlist.head)
reverselinkedlist.printList()

