from abc import ABC, abstractmethod

class ProductA(ABC):
    @abstractmethod
    def create_product_a(self):
        pass
    
class ProductB(ABC):
    @abstractmethod
    def create_product_b(self):
        pass
    
class ConcreteProductB1(ProductB): #b1represents the variant of product b
    def create_concrete_product_b(self): #represents the product -> sofa,chair
        return "concrete product b1"
    
class ConcreteProductB2(ProductB):
    def create_concrete_product_b(self):
        return "concrete product b2"

class ConcreteProductA1(ProductA):
    def create_concrete_product_a(self):
        return "concrete product a1"
    
class ConcreteProductA2(ProductA):
    def create_concrete_product_a(self):
        return "concrete product a2"
    

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass
    
    @abstractmethod
    def create_product_b(self):
        pass
    
class ConcreteFactory1(AbstractFactory): #represents the variant1 of all the products
    
    def create_product_a(self):
        return ConcreteProductA1()
    
    def create_product_b(self):
        return ConcreteProductB1()
    
class ConcreteFactory2(AbstractFactory): #represents the variant2 of all the products
    
    def create_product_a(self):
        return ConcreteProductA2()
    
    def create_product_b(self):
        return ConcreteProductB2()
    
# Concrete Factory -> represents the variants of a prod


def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")