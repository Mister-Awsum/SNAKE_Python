from Map import Map
from Obj import Obj
from ObjList import ObjList
import os

class GameMechs:   
    def __init__(self, rows = 10, cols = 10):
        self.__gameboard = Map(rows, cols)
        self.__playersnake = ObjList()
        
        test = Obj(7, 15, '@')
        
        self.__playersnake.insertHead(test)
        
    def clearscreen(self):
        # For Windows
        if os.name == 'nt':
            os.system('cls')
        # For Mac and Linux (posix systems)
        else:
            os.system('clear')
    
    def printGameBoard(self):
        #curr = self.__playersnake.getHead()
        
        #while(curr != None):
            #self.__gameboard.updateMap(curr)
            #curr = curr.getNext()
        
        self.clearscreen()
        self.__gameboard.printMap() 