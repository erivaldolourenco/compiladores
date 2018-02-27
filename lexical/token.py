# -*- coding: utf-8 -*-
from enum import Enum

""" Definir os valores das categorias """

class Category(Enum):
    ID = 0
    OPA = 1



class Token(object):

    def __init__(self, lexeme, category, position):
        #lexema e uma String
        self.lexeme = lexeme
        # categoria e um Enum
        self.category = category
        # posicao array[linha,clouna]
        self.position = position

    """Funcao que recebe um lexema e retorna a categoria"""
    def getToken(self, lexema):
    	for cat in Category:
    		if cat.value == lexema:
    			return cat
    		else:
    			print("Token nao foi encontrado")


if __name__ == '__main__':


	print(dir(Category))
	for cat in Category:
		print("CATEGORIA->"+str(cat))
		if cat == Category.ID:
			print("SIM")
		else:
			print("NAO")


	# print(Token().whatsClass('id'))
