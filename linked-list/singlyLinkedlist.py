
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, " -> ", end="")
            temp = temp.next
        print("end")

# Insert values at ends
linkedlist = LinkedList()
linkedlist.head = Node(1)
secodn_value = Node(2)
third_value = Node(1)

linkedlist.head.next = secodn_value
secodn_value.next = third_value

linkedlist.tail = third_value
# linkedlist.tail = linkedlist.head

linkedlist.printList()

# insert the value at first postion
next_head = linkedlist.head
linkedlist.head = Node(5)
next_head.next = secodn_value
linkedlist.head.next = next_head

linkedlist.printList()
    
