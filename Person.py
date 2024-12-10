#Jordan Marcelo CS 078 Test #2 Program
from datetime import datetime

class Person(object):
    def __init__(self, firstName, lastName, *args):
        self.firstName = firstName
        self.lastName = lastName
        self.birthday = datetime(1970, 1, 1) # default value
        self.setBirthday(*args)

    def setBirthday(self, *args):
        if len(args) >= 1 and isinstance(args[0], datetime):
            self.birthday = args[0]
        elif len(args) >= 3 and isinstance(args[0], int) and isinstance(args[1], int) and isinstance(args[2], int):
            self.birthday = datetime(month = args[0], day = args[1], year = args[2])

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getAge(self):
        return (datetime.today() - self.birthday).days//365

    def __str__(self):
        return f"{self.firstName} {self.lastName} is {self.getAge()} years old.".replace('  ', ' ')

class Student(Person):
    __current_id__ = 0
    masculine_identifiers = {'m', 'male', 'man', 'boy'}
    feminine_identifiers = {'f', 'female', 'woman', 'girl'}

    def __init__(self, firstName, lastName, gender, *args):
        super().__init__(firstName, lastName, *args)
        Student.__current_id__ += 1
        self.id = Student.__current_id__
        self.gender = str(gender)
        
        if self.gender.lower() in Student.masculine_identifiers:
            self.possessive_pronoun = 'his'
        elif self.gender.lower() in Student.feminine_identifiers:
            self.possessive_pronoun = 'her'
        else:
            self.possessive_pronoun = 'their'

    def getidNumber(self):
        return self.id

    def __str__(self):
        return super().__str__()[:-1] + f", and {self.possessive_pronoun} student ID is {self.getidNumber()}."

def main():
    Obama = Person('Barack', 'Obama')
    Obama.setBirthday(8, 4, 1961)
    print(Obama)

    Madonna = Person('Madonna', '')
    Madonna.setBirthday(datetime(year = 1958, month = 8, day = 16))
    print(Madonna)

    Abel = Student('Abel', 'Baker', 'M', datetime(year = 2001, month = 2, day = 1))
    print(Abel)

    Claudette = Student('Claudette', 'Davis', 'F', 5, 27, 2002)
    print(Claudette)

if __name__ == '__main__':
    main()