#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Explanation and schema in http://en.wikipedia.org/wiki/Builder_pattern
class Product:
    ''' Product with diferent parts to be created '''
    part1 = None
    part2 = None

    def __str__(self):
        return '[Product] [part1:%s] [part2:%s]'  % (self.part1, self.part2)

class Builder:
    ''' Abstract class '''
    product = None

    def buildPart1(self): pass

    def buildPart2(self): pass

    def createProduct(self):
        self.product = Product()

class ConcreteBuilder1(Builder):
    ''' One concrete builder '''
    def buildPart1(self):
        self.product.part1 = 'Part 1 of builder 1 built'

    def buildPart2(self):
        self.product.part2 = 'Part 2 of builder 1 built'

class ConcreteBuilder2(Builder):
    ''' Another concrete builder '''
    def buildPart1(self):
        self.product.part1 = 'Part 1 of builder 2 built'

    def buildPart2(self):
        self.product.part2 = 'Part 2 of builder 2 built'


class Director:
    ''' Director: It creates the product given a concrete builder '''
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.createProduct()
        self.builder.buildPart1()
        self.builder.buildPart2()

if __name__ == '__main__':
    # Concrete Builder 1
    concrete_builder = ConcreteBuilder1()
    director = Director(concrete_builder)
    director.construct()
    print director.builder.product

    # Concrete Builder 2
    concrete_builder = ConcreteBuilder2()
    director = Director(concrete_builder)
    director.construct()
    print director.builder.product
