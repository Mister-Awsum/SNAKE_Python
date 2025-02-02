from Obj import Obj

class ObjList:
    def __init__(self):
        self.__length = 0
        self.__chain = []
        
    def getHead(self):
        if self.__chain[0] == False:
            return False
        else:
            return self.__chain[0]

    def getElement(self, index):
        if self.__chain[index] == False:
            return False
        else:
            return self.__chain[index]
        
    def getTail(self):
        if self.__chain[-1] == False:
            return False
        else:
            return self.__chain[-1]
        
    def insertHead(self, obj):
        obj.setNext(self.getHead())
        self.__head = obj
        
        self.__length = self.__length + 1
        
    def append(self, obj):
        curr = self.__head
        
        while curr != None:
            curr = curr.getNext()
            
        curr.next = obj
        
        self.__tail = obj
        
        self.__length = self.__length + 1
        
    def removeTail(self):
        curr = self.__head
        
        while curr.getNext() != self.__tail:
            curr = curr.getNext()
            
        curr.next = None
        
        self.__tail = curr
        
        self.__length = self.__length - 1