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

    """Operadores de comparacao"""
    OP_IGU = 6
    OP_DIF = 7
    OP_MAIGU = 8
    OP_MEIGU = 9
    OP_ME = 10
    OP_MA = 11

    """Operadores Logicos"""
    OP_AND = 12
    OP_OR = 13
    OP_NOT = 14

    """Atribuição"""
    ATRIBUICAO = 15

    """Palavras Reservadas"""
    IF = 16
    ELSE = 17
    WHILE = 18
    FOR = 19
    BEGIN = 20
    VARIABLE = 21
    FUNCTION = 22
    RETURN = 23
    VOID = 24
    VARIABLE = 25

    """Tipos"""
    INT = 26
    CHAR = 27
    VECTOR = 28

    """Simbolos especiais"""
    ABR_CH = 29
    FEC_CH = 30
    ABR_PAR = 31
    FEC_PAR = 32
    ABR_COC = 33
    FEC_COC = 34
    SEP_VIRG = 35
    SEP_P_VIRG = 36
    SIMPLE_ASP = 37

    ID = 38
    CONST = 39
    PRINTOUT = 40

    UNKNOWN = 99
