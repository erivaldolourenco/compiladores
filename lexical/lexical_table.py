# -*- coding: utf-8 -*-

from .category_token import Category


class LexicalTable(object):

    def __init__(self):
        self.lexical_table = {
            '+': Category.OP_ADD,
            '-': Category.OP_SUB,
            '*': Category.OP_MULT,
            '/': Category.OP_DIV,
            '%': Category.OP_RET,
            '~': Category.OP_UNA,

            '==': Category.OP_IGU,
            '!=': Category.OP_DIF,
            '<=': Category.OP_MEIGU,
            '>=': Category.OP_MAIGU,
            '<': Category.OP_ME,
            '>': Category.OP_MA,

            '++': Category.OP_CONC,

            '&&': Category.OP_AND,
            '||': Category.OP_OR,
            '!': Category.OP_NOT,

            '=': Category.ATRIBUICAO,

            'if': Category.IF,
            'else': Category.ELSE,
            'while': Category.WHILE,
            'for': Category.FOR,
            'in': Category.IN,
            'do': Category.DO,
            'to': Category.TO,
            'begin': Category.BEGIN,
            'function': Category.FUNCTION,
            'return': Category.RETURN,
            'void': Category.VOID,
            'read': Category.READ,
            'put': Category.PUT,
            'break': Category.BREAK,

            'int': Category.INT,
            'float': Category.FLOAT,
            'char': Category.CHAR,
            'cchar': Category.CCHAR,
            'vector': Category.VECTOR,
            'bool': Category.BOOL,

            'true' : Category.TRUE,
            'false' : Category.FALSE,

            '{': Category.ABR_CH,
            '}': Category.FEC_CH,
            '(': Category.ABR_PAR,
            ')': Category.FEC_PAR,
            '[': Category.ABR_COC,
            ']': Category.FEC_COC,
            ',': Category.SEP_VIRG,
            ';': Category.SEP_P_VIRG,
            "'": Category.SIMPLE_ASP,

        }

    @classmethod
    def isSpecial(self, caracter):
        special = [' ', ',', '(', ')', '{', '}', '[', ']', ';', '+', '-', 
                   '*', '/', '%', '|', '=', "'", '\t', '\n', '&', '>', '<', '!', '#','$']
        return caracter in special





