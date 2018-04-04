# -*- coding: utf-8 -*-
from token import Token
from category_token import Category
from lexical import LexicalTable
position = [0, 0]


class Lexeme(object):

    def __init__(self, file):
        self.file = file

    def nextToken(self):
        with open(self.file) as fopen:
            filelines = fopen.readlines()
            line = filelines[position[0]]
            cont = True
            lexema = ''
            while cont:

                for i in range(position[1], int(line.__len__())):

                    if (line[i] != ' '):
                        lexema += line[i]

                    if line[i] == ' ':
                        position[1] += 1

                    elif line[i] == '+':
                        token = Token(
                            lexema, LexicalTable().lexical_table['+'], position)
                        cont = False
                        position[1] += 1
                        return token

                    elif line[i] == '-':
                        token = Token(
                            lexema, LexicalTable().lexical_table['-'], position)
                        cont = False
                        position[1] += 1
                        return token

                    elif line[i] == '*':
                        token = Token(
                            lexema, LexicalTable().lexical_table['*'], position)
                        cont = False
                        position[1] += 1
                        return token

                    elif line[i] == '/':
                        token = Token(
                            lexema, LexicalTable().lexical_table['/'], position)
                        cont = False
                        position[1] += 1
                        return token

                    elif line[i] == '%':
                        token = Token(
                            lexema, LexicalTable().lexical_table['%'], position)
                        cont = False
                        position[1] += 1
                        return token                    
                    elif line[i] == '>':
                        if line[i + 1] == '=':
                            lexema += line[i + 1]
                            token = Token(
                                lexema, LexicalTable().lexical_table[lexema], position)
                            cont = False
                            position[1] += 2
                            return token

                        else:
                            token = Token(
                                lexema, LexicalTable().lexical_table['>'], position)
                            cont = False
                            position[1] += 1
                            return token

                    elif line[i] == '<':
                        if line[i + 1] == '=':
                            lexema += line[i + 1]
                            token = Token(
                                lexema, LexicalTable().lexical_table[lexema], position)
                            cont = False
                            position[1] += 2
                            return token
                        else:
                            token = Token(
                                lexema, LexicalTable().lexical_table['<'], position)
                            cont = False
                            position[1] += 1
                            return token

                    elif line[i] == '!':
                        if line[i + 1] == '=':
                            lexema += line[i + 1]
                            token = Token(
                                lexema, LexicalTable().lexical_table[lexema], position)
                            cont = False
                            position[1] += 2
                            return token
                        else:
                            token = Token(
                                lexema, LexicalTable().lexical_table['!'], position)
                            cont = False
                            position[1] += 1
                            return token
                    elif line[i] == '&':
                        if line[i + 1] == '&':
                            lexema += line[i + 1]
                            token = Token(
                                lexema, LexicalTable().lexical_table[lexema], position)
                            cont = False
                            position[1] += 2
                            return token
                    elif line[i] == '|':
                        if line[i + 1] == '|':
                            lexema += line[i + 1]
                            token = Token(
                                lexema, LexicalTable().lexical_table[lexema], position)
                            cont = False
                            position[1] += 2
                            return token

                    elif line[i] == '=':
                        if line[i + 1] == '=':
                            lexema += line[i + 1]
                            token = Token(
                                lexema, LexicalTable().lexical_table[lexema], position)
                            cont = False
                            position[1] += 2
                            return token
                        else:
                            token = Token(
                                lexema, LexicalTable().lexical_table['='], position)
                            cont = False
                            position[1] += 1
                            return token

                    elif line[i] == '(':
                        token = Token(lexema, LexicalTable().lexical_table['('], position)
                        cont = False
                        position[1] += 1
                        return token

                    elif line[i] == ')':
                        token = Token(lexema, LexicalTable().lexical_table[')'], position)
                        cont = False
                        position[1] += 1
                        return token

                    elif line[i] == '{':
                        token = Token(
                            lexema, LexicalTable().lexical_table['{'], position)
                        cont = False
                        position[1] += 1
                        return token

                    elif line[i] == '}':
                        token = Token(
                            lexema, LexicalTable().lexical_table['}'], position)
                        cont = False
                        position[1] += 1
                        return token

                    elif line[i] == '[':
                        token = Token(
                            lexema, LexicalTable().lexical_table['['], position)
                        cont = False
                        position[1] += 1
                        return token

                    elif line[i] == ']':
                        token = Token(
                            lexema, LexicalTable().lexical_table[']'], position)
                        cont = False
                        position[1] += 1
                        return token

                    elif line[i] == ';':
                        token = Token(
                            lexema, LexicalTable().lexical_table[';'], position)
                        cont = False
                        position[1] += 1
                        return token

                    elif line[i] == ',':
                        token = Token(
                            lexema, LexicalTable().lexical_table[','], position)
                        cont = False
                        position[1] += 1
                        return token

                    elif line[i] == "'":
                        token = Token(
                            lexema, LexicalTable().lexical_table["'"], position)
                        cont = False
                        position[1] += 1
                        return token

                    elif line[i].isalnum():
                        if LexicalTable.isSpecial(line[i + 1]):
                            if lexema.isdigit():
                                token = Token(lexema, Category.CONST, position)
                                position[1] += 1
                                cont = False
                                return token
                            else:
                                try:
                                    token = Token(lexema, LexicalTable(
                                    ).lexical_table[lexema], position)
                                except Exception as e:
                                    token = Token(
                                        lexema, Category.ID, position)
                                position[1] += 1
                                cont = False
                                return token
                        else:
                            position[1] += 1

                    elif line[i] == '\t':
                        position[1] += 3

                    elif line[i] == "\n":
                        position[1] = 0
                        position[0] += 1
                        lexema = ''
                        line = filelines[position[0]]
                        break

                    else:
                        token = Token(lexema, Category.UNKNOWN, position)
                        position[1] += 1
                        return token

    def isToken(self):
        with open(self.file) as fopen:
            filelines = fopen.readlines()
        if(position[0] == (filelines.__len__() - 1) and position[1] == filelines[-1].__len__()):
            return False
        else:
            return True
