# Guttag 2e Introduction to code, tweaked
# a good example of inheritance

import datetime

# Person is the base class, parent to all the students
class Person(object):

    def __init__(self, name):
        
        """Create a person"""
        
        self.name = name
        try:
            lastBlank = name.rindex(' ')          # searching from end of string
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name                  # only has one name, like Cher
        self.birthday = None
 
    def getName(self):
        
        """Returns self's full name"""
        
        return self.name

    def getLastName(self):
        
        """Returns self's last name"""
        
        return self.lastName

    def setBirthday(self, birthdate):
        
        """Assumes birthdate is of type datetime.date
           Sets self's birthday to birthdate"""
        
        self.birthday = birthdate

    def getAge(self):
        
        """Returns self's current age in days"""
        
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        
        """Returns True if self's name is lexicographically
           less than other's name, and False otherwise"""
        
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        
        """Returns self's name"""
        
        return self.name

me  = Person('John K. Johnstone')
him = Person('Buzz Eugene Aldrin')
her = Person('Cher') # illustrating a name with no last name
print (me.getLastName())
print (him.getLastName())
print (her.getLastName())
him.setBirthday(datetime.date(1930, 1, 20))
her.setBirthday(datetime.date(1946, 5, 20))
print (him.getName(), 'is', him.getAge(), 'days old')
print (her.getName(), 'is', her.getAge(), 'days old')





pList = [me, him, her]
print ('\nOriginal list')
for p in pList:
    print (p)
pList.sort()                                        # uses the < we have defined
print ('\nSorted list')
for p in pList:
    print (p)



# UABPerson is inherited from Person
# UABPerson is a subclass of Person
# Person is the parent class or super class
class UABPerson (Person):
    
    nextIdNum = 0                                        # identification number
    
    def __init__(self, name):
        
        Person.__init__(self, name)
        self.idNum = UABPerson.nextIdNum
        UABPerson.nextIdNum += 1
        
    def getIdNum(self):
        return self.idNum
    
    def __lt__(self, other):
        return self.idNum < other.idNum

    def isStudent(self):
        return isinstance(self, Student)



p1 = UABPerson('Kathy Baier')
print (str(p1) + '\'s id number is ' + str(p1.getIdNum()))
p2 = UABPerson('Blaze the Dragon')
print (str(p2) + '\'s id number is ' + str(p2.getIdNum()))

print ('Is p1 < p2?', p1 < p2)


# 'dummy' class to allow 3-way split to UG/Grad/TransferStudent
class Student (UABPerson):
    pass

class UG (Student):
    
    def __init__(self, name, classYear):          # need to give the class year
        
        UABPerson.__init__(self, name)
        self.year = classYear
        
    def getClass(self):
        
        return self.year
    
class Grad (Student):

    def __init__(self, name, ugSchool):       # where did they go undergraduate?
        
        UABPerson.__init__(self, name)
        self.ugSchool = ugSchool
        
    def getUG (self):
        
        return self.ugSchool
    
class TransferStudent (Student):

    def __init__(self, name, fromSchool):
        UABPerson.__init__(self, name)
        self.fromSchool = fromSchool

    def getOldSchool(self):
        return self.fromSchool

p5 = Grad ('Ray Watts', 'UAB')
p6 = UG ('Graeme McDowell', 2002)
print (p6, 'is a graduate student: ', type(p6) == Grad)
print (p6, 'is an undergraduate student: ', type(p6) == UG)




