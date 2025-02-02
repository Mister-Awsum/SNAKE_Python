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
        
    def moveSnake(self, direction):
        if direction == 'w' or direction == 'W':
            self.__playersnake.insertHead(Obj(self.__playersnake.getHead().getX(), self.__playersnake.getHead().getY() - 1, '@'))
            self.__playersnake.removeTail()
            
        elif direction == 's' or direction == 'S':
            self.__playersnake.insertHead(Obj(self.__playersnake.getHead().getX(), self.__playersnake.getHead().getY() + 1, '@'))
            self.__playersnake.removeTail()
            
        elif direction == 'a' or direction == 'A':
            self.__playersnake.insertHead(Obj(self.__playersnake.getHead().getX() - 1, self.__playersnake.getHead().getY(), '@'))
            self.__playersnake.removeTail()
            
        elif direction == 'd' or direction == 'D':
            self.__playersnake.insertHead(Obj(self.__playersnake.getHead().getX() + 1, self.__playersnake.getHead().getY(), '@'))
            self.__playersnake.removeTail()
        
        
    def clearscreen(self):
        # For Windows
        if os.name == 'nt':
            os.system('cls')
        # For Mac and Linux (posix systems)
        else:
            os.system('clear')
    
    def printGameBoard(self):        
        self.clearscreen()
        self.__gameboard.printMap()
        
# Unit Test

game = GameMechs(20, 50)

game.clearscreen()
game.printGameBoard()