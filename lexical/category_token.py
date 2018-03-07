# -*- coding: utf-8 -*-
from enum import Enum

""" Definir os valores das categorias """


class Category(Enum):

    """Operadores aritimeticos"""
    OP_ADD = '+'
    OP_SUB = '-'
    OP_MULT = '*'
    OP_DIV = '/'
    OP_RET = '%'

    """Operadores de comparacao"""
    OP_IGU = '=='
    OP_DIF = '!='
    OP_MAIGU = '<='
    OP_MEIGU = '>='
    OP_ME = '<'
    OP_MA = '>'

    """Operadores Logicos"""
    OP_AND = '&&'
    OP_OR = '||'
    OP_NOT = '!'

    """Atribuição"""
    ATRIBUICAO = '='

    """Palavras Reservadas"""
    IF = 'if'
    ELSE = 'else'
    WHILE = 'while'
    FOR = 'for'
    BEGIN = 'begin'
    VARIABLE = 'variable'
    FUNCTION = 'function'
    RETURN = 'return'
    VOID = 'void'

    """Tipos"""
    INT = 'int'
    CHAR = 'char'
    VECTOR = 'vector'

    """Simbolos especiais"""
    ABR_CH = '{'
    FEC_CH = '}'
    ABR_PAR = '('
    FEC_PAR = ')'
    SEP_VIRG = ','
    SEP_P_VIRG = ';'
    ID = '[^A-Za-z0-9]'

    @classmethod
    def getCategory(self, lexeme):
        for ctg in Category:
            # print(ctg.value+"-----"+lexeme)
            if ctg.value == lexeme:
                return ctg
        if lexeme.isalnum():
            ctg = Category.ID
            return ctg
       

if __name__ == '__main__':

    print(Category.getCategory('int'))

    print("===============================")

    # print(list(Category))