# -*- coding: utf-8 -*-

from category_token import Category


class LexicalTable(object):

    def __init__(self):
        self.lexical_table = {
            '+': Category.OP_ADD,
            '-': Category.OP_SUB,
            '*': Category.OP_MULT,
            '/': Category.OP_DIV,
            '%': Category.OP_RET,

            '==': Category.OP_IGU,
            '!=': Category.OP_DIF,
            '<=': Category.OP_MEIGU,
            '>=': Category.OP_MAIGU,
            '<': Category.OP_ME,
            '>': Category.OP_MA,

            '&&': Category.OP_AND,
            '||': Category.OP_OR,
            '!': Category.OP_NOT,

            '=': Category.ATRIBUICAO,

            'if': Category.IF,
            'else': Category.ELSE,
            'while': Category.WHILE,
            'for': Category.FOR,
            'begin': Category.BEGIN,
            'variable': Category.VARIABLE,
            'function': Category.FUNCTION,
            'return': Category.RETURN,
            'void': Category.VOID,

            'int': Category.INT,
            'char': Category.CHAR,
            'vector': Category.VECTOR,

            '{': Category.ABR_CH,
            '}': Category.FEC_CH,
            '(': Category.ABR_PAR,
            ')': Category.FEC_PAR,
            '[': Category.ABR_COC,
            ']': Category.FEC_COC,
            ',': Category.SEP_VIRG,
            ';': Category.SEP_P_VIRG,
            "'": Category.SIMPLE_ASP,

            'put': Category.PRINTOUT,

        }

    @classmethod
    def isSpecial(self, caracter):
        special = [' ', ',', '(', ')', '{', '}', '[', ']', ';', '+', '-',
                   '*', '/', '%', '|', '=', "'", '\t', '\n', '&', '>', '<', '!', '#','$']
        return caracter in special





