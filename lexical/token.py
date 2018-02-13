# -*- coding: utf-8 -*-
from Enum import Enum

""" Definir os valores das categorias """

class Category(Enum):
    ID = 0
    OPA = 1


class Token(object):
 
    def __init__(self, lexeme, category, position):
        self.lexeme = lexeme
        self.category = category
        self.position = position
