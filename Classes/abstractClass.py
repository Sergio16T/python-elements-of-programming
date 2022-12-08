from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def move(self):
        print('Movement: ')
        pass

    @abstractmethod
    def sounds_like(self):
        pass


class Dog(Animal):

    def move(self):
        # super().move()
        print('the dog runs')

    def sounds_like(self):
        print('Woof')


pup = Dog()
pup.move()
pup.sounds_like()

