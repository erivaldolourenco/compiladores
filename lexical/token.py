# -*- coding: utf-8 -*-
from category_token import Category


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
        print('[' + str(self.position[0]) + ' , ' + str(self.position[1]) + '] ( ' +str(self.category) + ' ) { ' + self.lexeme + ' }')


if __name__ == '__main__':
    array = []
    array.append(3)
    array.append(45)
    caategory = Category.OP_ADD
    lexeme = '+'

    token = Token(lexeme, caategory, array)

    token.printToken()
