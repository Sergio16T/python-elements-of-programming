# class vs instance variables


# inheritance

# class DerivedClassName(BaseClassName):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>


# mixins

# self vs cls
# Self represents the current instance of the class
# Using the cls keyword, we represent that the method belongs to the class.
# We pass cls as an argument to the class methods. With cls, we attach the class method to the class.

# Using the cls keyword, we can only access the members of the class, whereas using the self keyword,
# we can access both the instance variables and the class attributes.

class Person:
    about = 'This class stores the name and age for a person as well as their element bending style'

    def __init__(self, name, element, age):
        self.name = name
        self.bendingStyle = element
        self.age = age

    def details(self):
        print(f"Person's name is {self.name}, they can {self.bendingStyle.lower()}bend and their age is {self.age}")
        print(self.about)

    @classmethod
    def info(cls):
        print(cls.about)


# Person.info()x

demoPerson = Person('Appa', 'Air', 18)

demoPerson.details()


class B:
    def method(self, arg):
        print(f"test {arg}")


class C(B):
    def method(self, arg):
        super().method(arg)    # This does the same thing as -->  super(C, self).method(arg)


cl = C()

# cl.method("try this")
