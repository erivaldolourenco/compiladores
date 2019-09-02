# -*- coding: utf-8 -*-
from enum import Enum

""" Definir os valores das categorias """


class Category(Enum):

    """Operadores aritimeticos"""
    OP_ADD = 1
    OP_SUB = 2
    OP_MULT = 3
    OP_DIV = 4
    OP_RET = 5
    OP_UNA = 6

    """Operadores de comparacao"""
    OP_IGU = 7
    OP_DIF = 8
    OP_MAIGU = 9
    OP_MEIGU = 10
    OP_ME = 11
    OP_MA = 12

    """Operador de concatenação"""

    OP_CONC = 13


    """Operadores Logicos"""
    OP_AND = 14
    OP_OR = 15
    OP_NOT = 16

    """Atribuição"""
    ATRIBUICAO = 17

    """Palavras Reservadas"""
    IF = 18
    ELSE = 19
    WHILE = 20
    FOR = 21
    BEGIN = 22
    FUNCTION = 23
    RETURN = 24
    VOID = 25
    READ = 26
    PUT = 27
    BREAK = 28
    # RETURN = 29
    

    """Tipos"""
    INT = 29
    FLOAT = 30
    CHAR = 31
    CCHAR = 32
    VECTOR = 33
    BOOL = 34

    """Simbolos especiais"""
    ABR_CH = 35
    FEC_CH = 36
    ABR_PAR = 37
    FEC_PAR = 38
    ABR_COC = 39
    FEC_COC = 40
    SEP_VIRG = 41
    SEP_P_VIRG = 42
    SIMPLE_ASP = 43

    ID = 44

    TRUE = 45
    FALSE = 46

    """ Constantes """
    CAD_CARACTER = 47
    # CONST_INT = 48
    # CONST_FLO = 49
    # CONST_CHA = 50
    CONST = 48


    UNKNOWN = 51
