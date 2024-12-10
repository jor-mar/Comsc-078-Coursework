#Jordan Marcelo COMSC 078 @ EVC, Object Oriented Programming assignment
import math
from datetime import datetime

class GeometricObject:
    """generic superclass for geometric shapes that have colors and can be filled, has getter
    and setter methods for each attribute"""
    def __init__(self, color = 'black', filled = False):
        self.dateCreated = datetime.now()
        self.color = color
        self.filled = filled

    def getDate(self):
        return self.dateCreated

    def getColor(self):
        return self.color

    def getFilled(self):
        return self.filled

    def setDate(self, date):
        self.dateCreated = date

    def setColor(self, color_string):
        self.color = color_string

    def setFilled(self, filled_boolean):
        self.filled = filled_boolean

    def __str__(self):
        return(f'A geometric object was created on {self.getDate()}\n'
               f'Color of geometric object is {self.getColor()}\n'
               f'Filled: {self.getFilled()}\n')


class Circle(GeometricObject):
    """circle subclass of geometric objects, has new attribute radius with appropriate getter
    and setter methods, includes getArea and getPerimeter. Default blue, filled, radius = 1.0"""
    def __init__(self, radius = 1.0):
        super().__init__('blue', True)
        self.radius = radius
        self.area, self.circumference = 0.0, 0.0

    def setRadius(self, radius = 1.0):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def getArea(self):
        self.area = math.pi * self.radius ** 2
        return self.area

    def getPerimeter(self):
        self.circumference = 2 * math.pi * self.radius
        return self.circumference

    def __str__(self):
        return (f'A circle was created on {(super().getDate())}\n'
                f'Color of circle is {super().getColor()}\n'
                f'Filled: {str(super().getFilled())}\n'
                f'The radius is {str(self.getRadius())}\n'
                f'The area is {str(self.getArea())}\n'
                f'The circumference is {str(self.getPerimeter())}\n')


class Rectangle(GeometricObject):
    """rectangle subclass of geometric objects, has new attributes width and height with appropriate getter
    and setter methods, includes getArea and getPerimeter. Default red, not filled, w = 4.0, h = 2.0"""
    def __init__(self, width = 4.0, height = 2.0):
        super().__init__('red', False)
        self.width = float(width)
        self.height = float(height)
        self.area, self.perimeter = 0.0, 0.0

    def getArea(self):
        self.area = self.width * self.height
        return self.area

    def setWidth(self, width):
        self.width = float(width)

    def setHeight(self, height):
        self.height = float(height)

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getPerimeter(self):
        self.perimeter = 2*(self.width+self.height)
        return self.perimeter

    def __str__(self):
        return(f'A rectangle was created on {str(super().getDate())}\n'
               f'Color of rectangle is {super().getColor()}\n'
               f'Filled: {str(super().getFilled())}\n'
               f'The width is {str(self.getWidth())}\n'
               f'The height is {str(self.getHeight())}\n'
               f'The area is {str(self.getArea())}\n'
               f'The perimeter is {str(self.getPerimeter())}\n')

def main():
    """Prompts the user for a circle radius, prints out the attributes of the circle of that radius
    and a default generated rectangle object"""
    radius = float(input('Enter the radius of your circle: '))
    print()
    print(str(Circle(radius)))
    print(str(Rectangle(4.0, 2.0)))

if __name__ == '__main__':
    main()