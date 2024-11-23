class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def traverse(self):
        if (self.head==None):
            print("list is empty")
            return 

        curr = self.head

        while curr != None:
            print(curr.data, end="-> ")
            curr = curr.next

    def insertHead(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def insertFromBack(self, value):
        newNode = Node(value)
        if self.head == None:
            return self.insertHead(value)

        curr = self.head

        while curr.next != None:
            curr = curr.next
        curr.next = newNode

    def inserAfterTarget(self, target, value):
        newNode = Node(value)
        flag = False
        if self.head == None:
            print("empty list")
            return

        curr = self.head

        while curr != None:
            if curr.data == target:
                flag = True
                break
            curr = curr.next
        if flag == True:
            newNode.next = curr.next
            curr.next = newNode
        else:
            print("element not found for insertion  ")

    def deleteFromFront(self):
        if self.head == None:
            print(" already  empty")
            return

        self.head = self.head.next

    def deleteFromLast(self):
        if self.head == None:
            print("already empty")
            return

        if self.head.next == None:  # agar 1 hi element hua toh usko delete karde 
            """self.head=None  ya phir delete from front call karde"""
            return self.deleteFromFront()

        curr = self.head
        while curr.next.next != None:
            curr = curr.next
        curr.next = None

      
    def deleteByTarget(self,target):
        if (self.head==None):
            print('empty ')
            return 
        
        if (self.head.data==target):
            # self.head=self.head.next

            return self.deleteFromFront()
        flag=False
        curr=self.head

        while (curr.next!=None):
            if (curr.next.data==target):
                flag=True
                break
            curr=curr.next

        if(flag==True):
            curr.next=curr.next.next


    def reverse(self):
        
       
      prev=None
      curr=self.head
        

      while(curr!=None):
          nextNode=curr.next
          curr.next=prev

          prev=curr
          curr=nextNode
        
      self.head=prev #Once the loop completes, 
      #curr is None, and prev points to the last node in the original list, which is now the new head of the reversed list.
            


l = LinkedList()

l.insertHead(5)
l.insertFromBack(10)
l.insertFromBack(20)
l.insertHead(1)


l.traverse()

print()

# l.inserAfterTarget(3, 55)

# l.deleteFromFront()
# l.deleteFromFront()
# l.deleteFromFront()
# l.deleteFromFront()


# l.deleteFromLast()
# l.deleteFromLast()
# l.deleteFromLast()
# l.deleteFromLast()

# l.deleteByTarget(10)
# l.deleteByTarget(20)
# l.deleteByTarget(1)


l.reverse()


l.traverse()

