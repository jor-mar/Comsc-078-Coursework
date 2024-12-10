# Jordan Marcelo CS 078 error assignment @ EVC
from fractions import Fraction


def readInt():
    txt = input('Enter an integer value: ')
    try:
        return int(txt)
    except ValueError as e:
        print(str(e))

def readVal(valType, promptMsg, errorMsg):
    x = input(f'{str(promptMsg)}: ')
    try:
        return valType(x)
    except ValueError:
        print(x, errorMsg)

def findIndefiniteArticle(txt):
    if txt[0] in {'a', 'e', 'i', 'o', 'u'}:
        return 'an'
    return 'a'

def testVal(valType):
    name = valType.__name__
    article = findIndefiniteArticle(name)
    x = readVal(valType,
                  f'Enter {article} {name}',
                  f'is not {article} {name}')
    print(f'{name} entered:', x)
    if isinstance(x, valType):
        print(f'The square of the {name} entered is:', x**2)
    print()

def main():
    test_types = [int, float, complex, Fraction]
    for test_type in test_types:
        testVal(test_type)

if __name__ == '__main__':
    main()