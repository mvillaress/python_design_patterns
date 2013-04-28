# Explanation and schema: http://en.wikipedia.org/wiki/Abstract_Factory
class AbstractProductA:
    pass

class ProductA1(AbstractProductA):
    def __init__(self):
        print 'Product A1 created'

class ProductA2(AbstractProductA):
    def __init__(self):
        print 'Product A2 created'



class AbstractProductB:
    pass

class ProductB1(AbstractProductB):
    def __init__(self):
        print 'Product B1 created'

class ProductB2(AbstractProductB):
    def __init__(self):
        print 'Product B2 created'




class AbstractFactory:
    @staticmethod
    def get_factory(factory):
        if factory == 1:
            return ConcreteFactory1()
        elif factory == 2:
            return ConcreteFactory2()

class ConcreteFactory1(AbstractFactory):
    def createProductA(self):
        return ProductA1()

    def createProductB(self):
        return ProductB1()

class ConcreteFactory2(AbstractFactory):
    def createProductA(self):
        return ProductA2()

    def createProductB(self):
        return ProductB2()


if __name__ == '__main__':
    factory = AbstractFactory.get_factory(1)
    factory.createProductA()
    factory.createProductB()
   
    factory = AbstractFactory.get_factory(2)
    factory.createProductA()
    factory.createProductB()