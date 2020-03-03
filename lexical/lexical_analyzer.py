# -*- coding: utf-8 -*-
from .token import Token
from .category_token import Category
from .lexical_table import LexicalTable
from tools.tools import Tools

import linecache
import re

position = [0, 0]


class Lexeme(object):

    def __init__(self, file):
        self.file = file
        self.nline = 1
        self.ncolumn = 0
        self.line = linecache.getline(self.file, self.nline)
        # print(str(self.nline).rjust(4) + " " + str(self.line), end='')
        Tools.print_f(str((str(self.nline).rjust(4) + " " + str(self.line))), self.file)


    def nextToken(self):

        lexema = ''
        # print(position[0])
        # print(position[1])

        for i in range(self.ncolumn, int(self.line.__len__())):
            # print(self.line[i])
            if self.line[i] != ' ':
                lexema += self.line[i]

            if self.line[i] == ' ':
                self.ncolumn += 1
                pass

            elif self.line[i - 1] == "'" and self.line[i - 2] == "(":
                j = i
                lexema = ''
                while self.line[j] != "'":
                    lexema += self.line[j]
                    j += 1
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, Category.CAD_CARACTER, position)
                self.ncolumn = j
                return token

            elif self.line[i] == '+':
                if self.line[i + 1] == '+':
                    lexema += self.line[i + 1]
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, Category.OP_CONC, position)
                    self.ncolumn += 2
                    return token
                else:
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, Category.OP_ADD, position)
                    self.ncolumn += 1
                    return token

            elif self.line[i] == '-':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, Category.OP_SUB, position)
                self.ncolumn += 1
                return token

            elif self.line[i] == '~':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, Category.OP_UNA, position)
                self.ncolumn += 1
                return token

            elif self.line[i] == '*':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, Category.OP_MULT, position)
                self.ncolumn += 1
                return token

            elif self.line[i] == '/':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, Category.OP_DIV, position)
                self.ncolumn += 1
                return token

            elif self.line[i] == '%':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, Category.OP_RET, position)
                self.ncolumn += 1
                return token
            elif self.line[i] == '>':
                if self.line[i + 1] == '=':
                    lexema += self.line[i + 1]
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, Category.OP_MAIGU, position)
                    self.ncolumn += 2
                    return token

                else:
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, Category.OP_MA, position)
                    self.ncolumn += 1
                    return token

            elif self.line[i] == '<':
                if self.line[i + 1] == '=':
                    lexema += self.line[i + 1]
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, Category.OP_MEIGU, position)
                    self.ncolumn += 2
                    return token
                else:
                    token = Token(lexema, Category.OP_ME, position)
                    self.ncolumn += 1
                    return token

            elif self.line[i] == '!':
                if self.line[i + 1] == '=':
                    lexema += self.line[i + 1]
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, Category.OP_DIF, position)
                    self.ncolumn += 2
                    return token
                else:
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, Category.OP_NOT, position)
                    self.ncolumn += 1
                    return token
            elif self.line[i] == '&':
                if self.line[i + 1] == '&':
                    lexema += self.line[i + 1]
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, Category.OP_AND, position)
                    self.ncolumn += 2
                    return token
            elif self.line[i] == '|':
                if self.line[i + 1] == '|':
                    lexema += self.line[i + 1]
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, Category.OP_OR, position)
                    self.ncolumn += 2
                    return token

            elif self.line[i] == '=':
                if self.line[i + 1] == '=':
                    lexema += self.line[i + 1]
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, Category.OP_IGU, position)
                    self.ncolumn += 2
                    return token
                else:
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, Category.ATRIBUICAO, position)
                    self.ncolumn += 1
                    return token

            elif self.line[i] == '(':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, Category.ABR_PAR, position)
                self.ncolumn += 1
                return token

            elif self.line[i] == ')':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, Category.FEC_PAR, position)
                self.ncolumn += 1
                return token

            elif self.line[i] == '{':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, Category.ABR_CH, position)
                self.ncolumn += 1
                return token

            elif self.line[i] == '}':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, Category.FEC_CH, position)
                self.ncolumn += 1
                return token

            elif self.line[i] == '[':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, Category.ABR_COC, position)
                self.ncolumn += 1
                return token

            elif self.line[i] == ']':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, Category.FEC_COC, position)
                self.ncolumn += 1
                return token

            elif self.line[i] == ';':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, Category.SEP_P_VIRG, position)
                self.ncolumn += 1
                return token

            elif self.line[i] == ',':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, Category.SEP_VIRG, position)
                self.ncolumn += 1
                return token

            elif self.line[i] == "'":
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, Category.SIMPLE_ASP, position)
                self.ncolumn += 1
                return token

            elif self.line[i].isalnum():

                if self.line[i - 1] == "'":
                    lexema = ''
                    k = i
                    token = None
                    while self.line[k] is not "'":
                        # print(self.line[k])
                        lexema += self.line[k]
                        token = Token(lexema, Category.CAD_CARACTER, position)
                        k += 1
                    self.ncolumn = k
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    return token

                j = i
                lexema = ''
                while not LexicalTable.isSpecial(self.line[j]):
                    lexema += self.line[j]
                    j += 1
                self.ncolumn = j
                position[0] = self.nline
                position[1] = self.ncolumn
                try:
                    token = Token(lexema, LexicalTable().lexical_table[lexema], position)
                except Exception as e:
                    if bool(re.search(r'\d.\d', lexema)):
                        token = Token(lexema, Category.CONST_FLO, position)
                    elif lexema.isdigit():
                        token = Token(lexema, Category.CONST_INT, position)
                    else:
                        token = Token(lexema, Category.ID, position)
                return token

            elif self.line[i] == '\t':
                self.ncolumn += 3

            elif self.line[i] == "\n":
                self.ncolumn = 0
                self.nline += 1
                self.line = linecache.getline(self.file, self.nline)
                # print(str(self.nline).rjust(4) + " " + str(self.line), end='')
                Tools.print_f(str((str(self.nline).rjust(4) + " " + str(self.line))), self.file)
                return self.nextToken()

            else:
                token = Token(lexema, Category.UNKNOWN, position)
                self.ncolumn += 1
                return token
