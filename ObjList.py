from Obj import Obj

class ObjList:
    def __init__(self):
        self.__head = None
        self.__tail = None
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
        obj.setNext(self.__head)
        self.__head = obj
        
        if self.__length == 0:
            self.__tail = obj
            self.__chain.append(obj)
        
        self.__length += 1
        
    def append(self, obj):
        if self.__length == 0:
            self.__head = obj
            self.__tail = obj
            
        else:
            self.__tail.setNext(obj)
            self.__tail = obj
            
        self.__chain.append(obj)
        
        self.__length += 1
        
    def removeTail(self):
        curr = self.__head
        
        while curr.getNext() != self.__tail:
            curr = curr.getNext()
            
        curr.next = None
        
        self.__tail = curr
        
        self.__length -= 1
        
# Unit Test

#objList = ObjList()

#obj1 = Obj(1, 2, 'A')
#obj2 = Obj(3, 4, 'B')
#obj3 = Obj(5, 6, 'C')

#objList.append(obj1)
#objList.append(obj2)
#objList.append(obj3)

#print("Head: ", objList.getHead().getSym(), "\n")
#print("Tail: ", objList.getTail().getSym(), "\n")
#print("Element 1: ", objList.getElement(1).getSym(), "\n")