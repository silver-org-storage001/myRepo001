class ListNode():

    def __init__(self, inValue):
        self.value = inValue
        self.next = None
        self.prev = None
    
    def getValue(self):
        return self.value
    
    def setValue(self, inValue):
        self.value = inValue

    def getNext(self):
        return self.next
    
    def setNext(self,newNext):
        self.next = newNext

    def getPrev(self):
        return self.prev
    
    def setPrev(self,newPrev):
        self.prev = newPrev

class LinkedList():
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # def __str__(self):
    #     return ListNode.value

    def __iter__(self):
        currNd = self.head
        while currNd !=None:
            yield currNd.value
            currNd = currNd.next
       
    def getHead(self):
        return self.head

    def getCount(self):
        return self.count

    def isEmpty(self):
        return (self.head == None)

    def insertFirst(self, newValue):
        newNd = ListNode(newValue)
        if self.isEmpty(): #if list is empty
            self.head = newNd
            self.tail = newNd
        else:
            newNd.setNext(self.head)
            self.head.setPrev(newNd)
            self.head = newNd
        self.count+=1
    
    def insertLast(self, newValue):
        newNd = ListNode(newValue)
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
        else:
            self.tail.setNext(newNd)
            newNd.setPrev(self.tail)
            self.tail = newNd
        self.count+=1

    def insertAsc(self, newValue):
        if self.isEmpty():
            self.insertFirst(newValue)
        else:
            newNd = ListNode(newValue)
            done = False
            curr = self.head
            while done == False:
                nextNd = curr.getNext()
                if (nextNd == None or newNd.getValue() < nextNd.getValue()):
                    if (curr.getValue() != newNd.getValue()): # to avoid duplicates
                        curr.setNext(newNd)
                        newNd.setNext(nextNd)
                    done = True
                curr = nextNd
    
    def peekFirst(self):
        if self.isEmpty():
            raise ValueError("List is empty")
        else:
            nodeValue = self.head.getValue()
        return nodeValue

    
    def peekLast(self):
        if self.isEmpty():
            raise ValueError("List is empty (peekLast)")
        else:
            currNd = self.head
            while currNd.getNext() != None:
                currNd = currNd.getNext()
            nodeValue = currNd.getValue()
        return nodeValue
    
    
    def removeFirst(self):
        if (self.isEmpty()):
            raise ValueError("List is Empty (removeFirst)")
        else:
            nodeValue = self.head.getValue()
            self.head = self.head.getNext()
            self.tail = self.tail.getPrev()
        self.count-=1
        return nodeValue
    
    def removeLast(self):
        if (self.isEmpty()):
            raise ValueError("List is empty (removeLast")
            
        else:
            if self.tail.getPrev() == None:
                nodeValue = self.tail.getValue()
                self.head = None
                self.tail = None
            else:
                nodeValue = self.tail.getValue()
                prev= self.tail.getPrev()
                self.tail.setNext(None)       
                self.tail = self.tail.getPrev()  
            self.count-=1   

                # prevNd = None
                # currNd = self.head
                # while currNd.getNext() != None:
                #     prevNd = currNd
                #     currNd = currNd.getNext()
                # prevNd.setNext(None)
                # nodeValue = currNd.getValue()
        return nodeValue
    
    def printf(self):
        while self.head!= None:
            print(self.head.getValue())
            self.head = self.head.getNext()

if __name__ == "__main__":
    print("This is LinkedList.py")


   

    