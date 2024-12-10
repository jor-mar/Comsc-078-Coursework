# Jordan Marcelo Generic Matrices Assignment for CS 076 @ EVC
# This program is designed to add and multiply matrices of integers and rational numbers

# note: this would be shorter, less complex, and more readable if the following were imported:
# from fractions import Fraction
# or
# from math import gcd
# in the case of the first import statement, the 'add' and 'multiply' methods
# could be delegated to the generic matrices superclass
# and there would be no need for a written Fraction class in this program
# in the case of the latter import, the static gcd method in the fraction class becomes unnecessary


class Fraction(object):
    """Represents a fraction as an automatically-simplifying object"""
    def __init__(self, num = 0, denominator = 1):
        self.numerator = int(num)
        self.denominator = int(denominator)
        self.__simplify__()

    @staticmethod
    def __gcd__(x, y):
        """Returns the least common multiple of two integers"""
        gcd = 1
        if x > y:
            smallest = y
        else:
            smallest = x
        for i in range(1, smallest+1):
            if x%i == 0 and y%i == 0:
                gcd = i
        return gcd

    def __simplify__(self):
        """Permanently simplifies fraction"""
        gcd = Fraction.__gcd__(self.numerator, self.denominator)
        self.numerator = int(self.numerator/gcd)
        self.denominator = int(self.denominator/gcd)

    def __add__(self, other):
        """Adds fraction to another and returns the result as a simplified Fraction object"""
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                          self.denominator * other.denominator)

    def __multiply__(self, other):
        """Multiplies fraction by another and returns the result as a simplified Fraction object"""
        return Fraction(self.numerator * other.numerator,
                          self.denominator * other.denominator)

    def __str__(self):
        """Expresses the fraction object as a string"""
        return str(self.numerator) + '/' + str(self.denominator)


class GenericMatrix(object):
    """Abstract class that operates on matrices with the same types of numbers"""
    def __init__(self, *args):
        self.rows = len(args)
        self.columns = len(args[0])
        self.raw = args
        #for arg in args:
            #assert(len(arg) == self.columns, 'incomplete matrix')

    def __add__(self, num1, num2):
        """Adds two elements of drawn from matrices"""
        # This abstract method returns nothing as it will be overridden in a concrete subclass

    def __mul__(self, num1, num2):
        """For multiplying two elements drawn from matrices"""
        # This abstract method returns nothing as it will be overridden in a concrete subclass

    def __zero__(self):
        """Abstract method for defining the zero element for the type of matrix."""
        # The abstract method returns nothing as it will be overridden in the concrete subclass

    def __addMatrix__(self, m2):
        """Adds two matrices with the same types of elements and returns the resulting matrix."""
        #assert(self.rows == m2.rows and self.columns == m2.columns and isinstance(m2, type(self)), 'incompatible matrices')
        new_data = []
        for row in range(self.rows):
            new_row = []
            for column in range(self.columns):
                new_row.append(self.__add__(self.raw[row][column], m2.raw[row][column]))
            new_data.append(new_row)
        return type(self)(*new_data)

    def __multiplyMatrix__(self, m2):
        """Multiplies two matrices with the same types of elements and returns the resulting matrix."""
        #assert (self.columns == m2.rows and isinstance(m2, type(self)), 'incompatible matrices')
        new_data = [[self.__zero__() for _ in range(m2.columns)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(m2.columns):
                for k in range(m2.rows):
                    new_data[i][j] = self.__add__(new_data[i][j], self.__mul__(self.raw[i][k], m2.raw[k][j]))
        return type(self)(*new_data)

    def __str__(self):
        """Returns the string representation of the result"""
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(str(self.raw[i][j]))
            result.append(row)
        return '\n'.join(str(row) for row in result)


class IntegerMatrix(GenericMatrix):
    """Allows you to add and multiply the elements in an IntegerMatrix"""
    def __init__(self, *args):
        super().__init__(*args)
        #for arg in args:
            #assert(type(arg[0]) == int, 'improper integer matrix declared')

    def __add__(self, num1, num2):
        """Adds two integers and return the sum"""
        return num1 + num2

    def __mul__(self, num1, num2):
        """Multiplies two integers and returns the product"""
        return num1 * num2

    def __zero__(self):
        """Returns 0 for as an integer"""
        return 0


class RationalMatrix(GenericMatrix):
    """Allows you to add and multiply two elements in a RationalMatrix"""
    def __init__(self, *args):
        super().__init__(*args)
        new_raw = []
        for arg in args:
            #assert(type(arg[0]) == Fraction or type(arg[0]) == int, 'improper rational matrix declared')
            new_row = [Fraction(x) if not isinstance(x, Fraction) else x for x in arg]
            new_raw.append(new_row)
        self.raw = new_raw

    def __add__(self, num1, num2):
        """Add and return the sum of two rational numbers"""
        return num1.__add__(num2)

    def __mul__(self, num1, num2):
        """Multiply and return the product of two rational numbers"""
        return num1.__multiply__(num2)

    def __zero__(self):
        """Returns the zero for rational numbers (0/1)."""
        return Fraction()


def print_matrix_operations(m1, m2):
    print(str(m1) + '\n+\n' + str(m2) + '\n=\n' + str(m1.__addMatrix__(m2)), '\n')
    print(str(m1) + '\n*\n' + str(m2) + '\n=\n' + str(m1.__multiplyMatrix__(m2)), '\n')

def main():
    m1 = IntegerMatrix([1,2,3],
                       [4,5,6],
                       [1,1,1])
    m2 = IntegerMatrix([1,1,1],
                       [2,2,2],
                       [0,0,0])
    print_matrix_operations(m1, m2)

    m1 = RationalMatrix([Fraction(1,5),Fraction(1,6),Fraction(1,7)],
                       [Fraction(2,5),Fraction(1,3),Fraction(2,7)],
                       [Fraction(3,5),Fraction(1,2),Fraction(3,7)])
    m2 = RationalMatrix([Fraction(1,6),Fraction(1,7),Fraction(1,8)],
                       [Fraction(1,3),Fraction(2,7),Fraction(1,4)],
                       [Fraction(1,2),Fraction(3,7),Fraction(3,8)])
    print_matrix_operations(m1, m2)

if __name__ == '__main__':
    main()