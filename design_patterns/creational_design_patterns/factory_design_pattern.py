'''
a creational design pattern

there are actually 2 

- product 
- creator

we will be using the idea of abstraction and the interfaces t



'''
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def doStuff(self):
        pass


class ConcreteProduct1(Product):
    def doStuff(self):
        return "stuff method of ConcreteProduct1"

class ConcreteProduct2(Product):
    def doStuff(self):
        return "stuff method of ConcreteProduct2"
    
class Creator(ABC):
    
    @abstractmethod
    def factory_method(self):
        pass
    
    def showOperations(self):
        product = self.factory_method()
        result = product.doStuff()
        return result
    
class ConcreteCreator1(Creator):
    
    def factory_method(self):
        return ConcreteProduct1()
    
class ConcreteCreator2(Creator):
    
    def factory_method(self):
        return ConcreteProduct2()
    

def main(creator: Creator):
    res = creator.showOperations()
    print(res)
    
if __name__ == "__main__":
    main(ConcreteCreator1())
    main(ConcreteCreator2())


'''
# questions
- things i don't get still is that why 
    - what problem does the factory design pattern helps in resolving.
    - can i identify a use case where it can be used better. Suppose in my use case.
    - 

'''