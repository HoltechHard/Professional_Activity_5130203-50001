# basic structure of class

import math

class Point:    
    def __init__(self, x: float, y: float) -> None:
        """
        constructor of Point class
        Keyword arguments:
        argument -- 
        : param x: float x-coordinate
        : param y: float y-coordinate
        """        
        self.move(x, y)

    # function to move in 2d space
    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    
    # reset point to origin of coordinates
    def reset(self) -> None:
        self.move(0, 0)
    
    # function to calculate euclidean distance
    def calculate_distance(self, other: "Point") -> float:
        """        
        Keyword arguments:
        argument -- Point object
        Return: float distance
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)        
###

def main():
    point1 = Point(10, 8)
    point2 = Point(5, 0)
    print("1st dist = ", point1.calculate_distance(point2))
    point1.reset()
    print("2nd dist = ", point2.calculate_distance(point1))
    point1.move(3, 4)
    print("3rd dist = ", point1.calculate_distance(point2))

if __name__ == "__main__":
    main()

