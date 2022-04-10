class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Palindrome:
    def __init__(self) -> None:
        self.head = None

    def add_back(self,data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            temp = self.head
            while(temp):
                if temp.next == None:
                    newNode = Node(data)
                    temp.next = newNode
                    break
                temp = temp.next
                
            
    def add_front(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode         

    def reverse(self, head):
        if head == None or head.next == None:
            return head

        newHead = self.reverse(head.next)
        headNext = head.next
        headNext.next = head
        head.next = None
        # print("newHead.data =", newHead.data)

        return newHead


    def middle(self,head):
        slow = head
        fast = head
        
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next 
            # print(slow)
        return slow
    
    def palindrome(self,head):
        current = self.head
        # print("current : ", current)
        if head == None:
            return True

        mid = self.middle(head)
        # print("mid.data = ", mid.data)
        # print("mid.next.data:", mid.next.data)
        last = self.reverse(mid.next)
        
        # print("last.data", last.data)
        while(last != None):
            if last.data != current.data:
                print(False)
                return
            # print("test")
            last = last.next 
            current = current.next

        print(True)
        return


    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, "->", end="")
            temp = temp.next
        print("end")




p = Palindrome()
p.add_front(2)
p.add_front(20)
p.add_front(22)
p.add_front(12)
p.add_front(82)

p.printList()
p.head = p.palindrome(p.head)
