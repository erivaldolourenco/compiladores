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
    VARIABLE = 'variable'

    """Tipos"""
    INT = 'int'
    CHAR = 'char'
    VECTOR = 'vector'

    """Simbolos especiais"""
    ABR_CH = '{'
    FEC_CH = '}'
    ABR_PAR = '('
    FEC_PAR = ')'
    ABR_COC = '['
    FEC_COC = '['
    SEP_VIRG = ','
    SEP_P_VIRG = ';'
    SIMPLE_ASP = "'"
    ID = '[^A-Za-z0-9]'
    UNKNOWN = 999

    @classmethod
    def getCategory(self, lexeme):
        for ctg in Category:
            # print(ctg.value+"-----"+lexeme)
            if ctg.value == lexeme:
                return ctg
        if lexeme.isalnum():
            ctg = Category.ID
            return ctg
        else:
            ctg = Category.UNKNOWN
            return ctg
    
    @classmethod
    def isSpecial(self, caracter):
        special = [' ',',','(',')','{','}','[',']',';','+','-','*','/','%','|','=',"'",'\t','\n','&','>','<','!']
        for c in special:
            if caracter == c:
                return True

        return False

if __name__ == '__main__':

    print(Category.isSpecial('\n'))

    print("===============================")

    # print(list(Category))