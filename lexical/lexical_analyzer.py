# -*- coding: utf-8 -*-
from .token import Token
from .category_token import Category
from .lexical_table import LexicalTable
import linecache

position = [0,0]
# teste = "-------"
class Lexeme(object):
    
    def __init__(self, file):
        self.file = file
        self.nline = 1
        self.ncolumn = 0

    def nextToken(self):
        
        line = linecache.getline(self.file, self.nline)

        # print "=================LINHA"
        # print self.nline
        # print line
        # print "=================NUMERO"

        lexema = ''

        for i in range(self.ncolumn, int(line.__len__())):

            if (line[i] != ' '):
                lexema += line[i]

            if line[i] == ' ':
                self.ncolumn += 1

            elif line[i] == '+':
                if line[i + 1] == '+':
                    lexema += line[i + 1]
                    token = Token(lexema, LexicalTable().lexical_table[lexema], position)
                    self.ncolumn += 2
                    return token
                else:
                    token = Token(lexema, LexicalTable().lexical_table['+'], position)
                    self.ncolumn += 1
                    return token

            elif line[i] == '-':
                token = Token(lexema, LexicalTable().lexical_table['-'], position)
                self.ncolumn += 1
                return token

            elif line[i] == '~':
                token = Token(lexema, LexicalTable().lexical_table['~'], position)
                self.ncolumn += 1
                return token

            elif line[i] == '*':
                token = Token(lexema, LexicalTable().lexical_table['*'], position)
                self.ncolumn += 1
                return token

            elif line[i] == '/':
                token = Token(lexema, LexicalTable().lexical_table['/'], position)
                self.ncolumn += 1
                return token

            elif line[i] == '%':
                token = Token(lexema, LexicalTable().lexical_table['%'], position)
                self.ncolumn += 1
                return token                    
            elif line[i] == '>':
                if line[i + 1] == '=':
                    lexema += line[i + 1]
                    token = Token(lexema, LexicalTable().lexical_table[lexema], position)
                    self.ncolumn += 2
                    return token

                else:
                    token = Token(lexema, LexicalTable().lexical_table['>'], position)
                    self.ncolumn += 1
                    return token

            elif line[i] == '<':
                if line[i + 1] == '=':
                    lexema += line[i + 1]
                    token = Token(lexema, LexicalTable().lexical_table[lexema], position)
                    self.ncolumn += 2
                    return token
                else:
                    token = Token(lexema, LexicalTable().lexical_table['<'], position)
                    self.ncolumn += 1
                    return token

            elif line[i] == '!':
                if line[i + 1] == '=':
                    lexema += line[i + 1]
                    token = Token(lexema, LexicalTable().lexical_table[lexema], position)
                    self.ncolumn += 2
                    return token
                else:
                    token = Token(lexema, LexicalTable().lexical_table['!'], position)
                    self.ncolumn += 1
                    return token
            elif line[i] == '&':
                if line[i + 1] == '&':
                    lexema += line[i + 1]
                    token = Token(lexema, LexicalTable().lexical_table[lexema], position)
                    self.ncolumn += 2
                    return token
            elif line[i] == '|':
                if line[i + 1] == '|':
                    lexema += line[i + 1]
                    token = Token(lexema, LexicalTable().lexical_table[lexema], position)
                    self.ncolumn += 2
                    return token

            elif line[i] == '=':
                if line[i + 1] == '=':
                    lexema += line[i + 1]
                    token = Token(lexema, LexicalTable().lexical_table[lexema], position)
                    self.ncolumn += 2
                    return token
                else:
                    token = Token(lexema, LexicalTable().lexical_table['='], position)
                    self.ncolumn += 1
                    return token

            elif line[i] == '(':
                token = Token(lexema, LexicalTable().lexical_table['('], position)
                self.ncolumn += 1
                return token

            elif line[i] == ')':
                token = Token(lexema, LexicalTable().lexical_table[')'], position)
                self.ncolumn += 1
                return token

            elif line[i] == '{':
                token = Token(lexema, LexicalTable().lexical_table['{'], position)
                self.ncolumn += 1
                return token

            elif line[i] == '}':
                token = Token(lexema, LexicalTable().lexical_table['}'], position)
                self.ncolumn += 1
                return token

            elif line[i] == '[':
                token = Token(lexema, LexicalTable().lexical_table['['], position)
                self.ncolumn += 1
                return token

            elif line[i] == ']':
                token = Token(lexema, LexicalTable().lexical_table[']'], position)
                self.ncolumn += 1
                return token

            elif line[i] == ';':
                token = Token(
                    lexema, LexicalTable().lexical_table[';'], position)
                self.ncolumn += 1
                return token

            elif line[i] == ',':
                token = Token(lexema, LexicalTable().lexical_table[','], position)
                self.ncolumn += 1
                return token

            elif line[i] == "'":
                token = Token(lexema, LexicalTable().lexical_table["'"], position)
                self.ncolumn += 1
                return token

            elif line[i].isalnum():
                if LexicalTable.isSpecial(line[i + 1]):
                    if lexema.isdigit():
                        token = Token(lexema, Category.CONST, position)
                        self.ncolumn += 1
                        return token
                    else:
                        try:
                            token = Token(lexema, LexicalTable().lexical_table[lexema], position)
                        except Exception as e:
                            token = Token(lexema, Category.ID, position)
                        self.ncolumn += 1
                        return token
                else:
                    self.ncolumn += 1

            elif line[i] == '\t':
                self.ncolumn += 3

            elif line[i] == "\n":
                self.ncolumn = 0
                self.nline += 1
                return self.nextToken()

            else:
                token = Token(lexema, Category.UNKNOWN, position)
                self.ncolumn += 1
                return token
