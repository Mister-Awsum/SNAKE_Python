import os
from Obj import Obj

class Map:
    def __init__(self, rows=10, cols=10):
        self.__rows = rows
        self.__cols = cols
        self.__array2D = [[" " for _ in range(self.__cols)] for _ in range(self.__rows)]
        
        for i in range(self.__rows):
            for j in range(self.__cols):
                if i == 0 or i == self.__rows - 1 or j == 0 or j == self.__cols - 1:
                    self.__array2D[i][j] = "#"
                    
                else:
                    self.__array2D[i][j] = " "
                    
    def updateMap(self, obj):
        y = obj.getY()
        x = obj.getX()

        self.__array2D[y][x] = obj.getSym()

    def clear_screen():
        # For Windows
        if os.name == 'nt':
            os.system('cls')
        # For macOS and Linux
        else:
            os.system('clear')
            
    def printMap(self):
        row = ""
        
        for i in range(self.__rows):
            for j in range(self.__cols):
                row = row + self.__array2D[i][j]
            
            row = row + "\n"
            
        print(row)
        
# Unit Test

#map = Map(10, 10)

#obj = Obj(4, 2, '@')

#map.updateMap(obj)

#map.printMap()