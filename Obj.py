class Obj:
    def __init__(self, x = 0, y = 0, symbol = '?'):
        self.__x = x
        self.__y = y
        self.__symbol = symbol
        self.next = None
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getSym(self):
        return self.__symbol
    
    def getNext(self):
        return self.next
    
    def setX(self, x):
        self.__x = x
        
    def setY(self, y):
        self.__y = y
        
    def setSym(self, symbol):
        self.__symbol = symbol
        
    def setNext(self, obj):
        self.next = obj
        
    def copyObj(self, obj):
        self.setX(obj.getX())
        self.setY(obj.getY())
        self.setSym(obj.getSym())
        
    def isEqual(self, obj):
        if(self.getX() == obj.getX() and self.getY() == obj.getY()):
            return True
        
        else:
            return False