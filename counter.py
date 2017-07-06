#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com

from collections import Counter
from collections import namedtuple

#Item = namedtuple("Item","name price")

class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __repr__(self):
        return "({},{})".format(self.name,self.price)


apple_1 = Item("apple",5)
apple_2 = Item("apple",5)
apple_3 = Item("apple",5)
orange = Item("orange",3)
lemon = Item("lemon",2)



#fruits_case = [apple] * 5 + [orange] * 3 + [lemon] * 6
fruits_case = [apple_1,apple_2,apple_3,orange,lemon]

fruits_case[0].name = "APPLE"



for item in fruits_case:
    print(id(item))

print(fruits_case[0] is fruits_case[1])

print(Counter(fruits_case))

print(fruits_case[0],fruits_case[1])