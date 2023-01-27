class Node:
    def __init__(self, val=None , next = None):
        self.val = val
        self.next = next
        
        

class MyLinkedList:
    def __init__(self):
        self.head= None
        

    def get(self, index: int) -> int:
        if not self.head:
            return -1
        else:
            i = 0
            node = self.head
            while not index == i and node:
                node = node.next
                i += 1
            if node:
                return node.val
            else:
                return -1
            

        
        

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = Node (val)
        else:
            self.head = Node(val , self.head)

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node (val)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if not self.head and index != 0:
            pass
        elif not self.head and index == 0:
            self.head = Node(val)
            self.pnt()
            return
        else:
            node = self.head
            i = 0
            while node.next and not index - i == 1:
                node = node.next
                i = i +1 
            if index-i == 1:
                temp = node.next
                node.next = Node(val , temp)
            if index - i == 0:
                self.head = Node(val , self.head)
        self.pnt()
                
        

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            pass
        if index == 0:
            self.head = self.head.next
        else:
            node = self.head
            i = 0
            node = self.head
            i = 0
            while node.next and not index - i == 1:
                node = node.next
                i = i +1 
            if index-i == 1 and node.next:
                temp = node.next.next
                node.next = temp
        self.pnt()
    def pnt(self):
        node = self.head
        while node:
            print(node.val , end = " ")
            node = node.next
        print()
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)