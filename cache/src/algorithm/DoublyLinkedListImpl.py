# decide what all the methods this doubly linkedlist should have.
import sys
sys.path.append("C:/Users/mridul/OneDrive/Documents/GitHub/machinecoding/")
from cache.src.algorithm.Node import LinkedListNode
from cache.src.algorithm.DoubleLinkedList import DoubleLinkedList

class DoublyLinkedList(DoubleLinkedList):
    def __init__(self):
        
        self.head = None
    
    def insertAtEnd(self, data):
        newNode = LinkedListNode(data)
        temp = self.head
        if temp is None:
            self.head  = newNode
        else:
            while temp.next:  
                temp=temp.next  
            temp.next=newNode
            newNode.prev = temp

    def removeAtBeginning(self):
        temp  = self.head
        if temp:
            self.head = self.head.next
            self.head.prev = None
        #del temp 
        return temp.data
    
    def linkedListSize(self):
        self.count = 0
        temp  = self.head
        while temp:
            self.count+=1
            temp = temp.next
        return self.count
    
    def printDll(self):
        curr = self.head
        li = []
        while curr is not None:
            li.append(curr.data)
            curr = curr.next
    
# if __name__ == "__main":
#     d = DoublyLinkedList()
#     print("double")
#     d.insertAtEnd(1)
#     d.insertAtEnd(2)
#     d.insertAtEnd(3)
#     d.insertAtEnd(4)
#     d.insertAtEnd(5)
#     print("double5")
#     d.printDll()
#     d.removeAtBeginning()
#     d.linkedListSize()
        