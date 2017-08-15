#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
def Run_twice(Animal):
    Animal.run()
    Animal.run()
dog=Dog()
cat=Cat()
dog.run()
cat.run()
tt=Tortoise()
tt.run()
Run_twice(dog)
Run_twice(cat)
Run_twice(tt)

print(isinstance(dog,Dog))
print(isinstance(dog,Animal))
print(isinstance(cat,Cat))
print(isinstance(cat,Animal))
print(isinstance(tt,Tortoise))
print(isinstance(tt,Animal))
aa=Animal()
print(isinstance(aa,Animal))
print(isinstance(aa,Cat))
print(isinstance(aa,Dog))
def Run_twice(Cat):
    Cat.run()
    Cat.run()
Run_twice(aa)