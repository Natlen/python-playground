class Animal:
    def __init__(self, name : str) -> None:
        self._name = name
    def sound(self) -> None:
        raise NotImplemented
    
class Dog(Animal):
    def __init__(self, name : str) -> None:
        super().__init__(name)
        self.__noise = 'Woof'
    def sound(self):
        print(f'{self._name} goes {self.__noise}')


class Cat(Animal):
    def __init__(self, name : str) -> None:
        super().__init__(name)
        self.__noise = 'Meow'
    def sound(self):
        print(f'{self._name} goes {self.__noise}')

def f(a : Animal) -> None:
    a.sound()

d = Dog('Doggoie')
c = Cat('Cattie')
f(d)
f(c)