# -*- coding: utf-8 -*-
from .category_token import Category


class Token(object):

    def __init__(self, lexeme, category, position):
        # lexema e uma String
        self.lexeme = lexeme
        # categoria e um Enum
        self.category = category
        # posicao array[linha,coluna]
        self.position = position

    """Metodo que imprime o Token"""

    def printToken(self):
        print('        [' + str(self.position[0]).zfill(4) + ', ' + str(self.position[1]).zfill(4) + '] (' +
              str(self.category.value).zfill(4) + ', ' + str(self.category.name).ljust(20) + ') {' + self.lexeme + '}')
