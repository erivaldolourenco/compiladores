# -*- coding: utf-8 -*-
from .token import Token
from .category_token import Category
from .lexical_table import LexicalTable
import linecache

position = [0,0]
class Lexeme(object):
    
    def __init__(self, file):
        self.file = file
        self.nline = 1
        self.ncolumn = 0
        self.line = linecache.getline(self.file, self.nline)

    def nextToken(self):
        
        # line = linecache.getline(self.file, self.nline)

        lexema = ''

        for i in range(self.ncolumn, int(self.line.__len__())):

            if (self.line[i] != ' '):
                lexema += self.line[i]
                

            if self.line[i] == ' ':
                self.ncolumn += 1
                pass

            elif self.line[i] == '+':
                if self.line[i + 1] == '+':
                    lexema += self.line[i + 1]
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, LexicalTable().lexical_table[lexema], position)
                    self.ncolumn += 2
                    return token
                else:
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, LexicalTable().lexical_table['+'], position)
                    self.ncolumn += 1
                    return token

            elif self.line[i] == '-':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, LexicalTable().lexical_table['-'], position)
                self.ncolumn += 1
                return token

            elif self.line[i] == '~':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, LexicalTable().lexical_table['~'], position)
                self.ncolumn += 1
                return token

            elif self.line[i] == '*':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, LexicalTable().lexical_table['*'], position)
                self.ncolumn += 1
                return token

            elif self.line[i] == '/':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, LexicalTable().lexical_table['/'], position)
                self.ncolumn += 1
                return token

            elif self.line[i] == '%':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, LexicalTable().lexical_table['%'], position)
                self.ncolumn += 1
                return token                    
            elif self.line[i] == '>':
                if self.line[i + 1] == '=':
                    lexema += self.line[i + 1]
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, LexicalTable().lexical_table[lexema], position)
                    self.ncolumn += 2
                    return token

                else:
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, LexicalTable().lexical_table['>'], position)
                    self.ncolumn += 1
                    return token

            elif self.line[i] == '<':
                if self.line[i + 1] == '=':
                    lexema += self.line[i + 1]
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, LexicalTable().lexical_table[lexema], position)
                    self.ncolumn += 2
                    return token
                else:
                    token = Token(lexema, LexicalTable().lexical_table['<'], position)
                    self.ncolumn += 1
                    return token

            elif self.line[i] == '!':
                if self.line[i + 1] == '=':
                    lexema += self.line[i + 1]
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, LexicalTable().lexical_table[lexema], position)
                    self.ncolumn += 2
                    return token
                else:
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, LexicalTable().lexical_table['!'], position)
                    self.ncolumn += 1
                    return token
            elif self.line[i] == '&':
                if self.line[i + 1] == '&':
                    lexema += self.line[i + 1]
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, LexicalTable().lexical_table[lexema], position)
                    self.ncolumn += 2
                    return token
            elif self.line[i] == '|':
                if self.line[i + 1] == '|':
                    lexema += self.line[i + 1]
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, LexicalTable().lexical_table[lexema], position)
                    self.ncolumn += 2
                    return token

            elif self.line[i] == '=':
                if self.line[i + 1] == '=':
                    lexema += self.line[i + 1]
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, LexicalTable().lexical_table[lexema], position)
                    self.ncolumn += 2
                    return token
                else:
                    position[0] = self.nline
                    position[1] = self.ncolumn
                    token = Token(lexema, LexicalTable().lexical_table['='], position)
                    self.ncolumn += 1
                    return token

            elif self.line[i] == '(':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, LexicalTable().lexical_table['('], position)
                self.ncolumn += 1
                return token

            elif self.line[i] == ')':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, LexicalTable().lexical_table[')'], position)
                self.ncolumn += 1
                return token

            elif self.line[i] == '{':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, LexicalTable().lexical_table['{'], position)
                self.ncolumn += 1
                return token

            elif self.line[i] == '}':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, LexicalTable().lexical_table['}'], position)
                self.ncolumn += 1
                return token

            elif self.line[i] == '[':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, LexicalTable().lexical_table['['], position)
                self.ncolumn += 1
                return token

            elif self.line[i] == ']':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, LexicalTable().lexical_table[']'], position)
                self.ncolumn += 1
                return token

            elif self.line[i] == ';':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, LexicalTable().lexical_table[';'], position)
                self.ncolumn += 1
                return token

            elif self.line[i] == ',':
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, LexicalTable().lexical_table[','], position)
                self.ncolumn += 1
                return token

            elif self.line[i] == "'":
                position[0] = self.nline
                position[1] = self.ncolumn
                token = Token(lexema, LexicalTable().lexical_table["'"], position)
                self.ncolumn += 1
                return token

            elif self.line[i].isalnum():
                if LexicalTable.isSpecial(self.line[i + 1]):
                    if lexema.isdigit():
                        position[0] = self.nline
                        position[1] = self.ncolumn
                        token = Token(lexema, Category.CONST, position)
                        self.ncolumn += 1
                        return token
                    else:
                        position[0] = self.nline
                        position[1] = self.ncolumn
                        try:
                            token = Token(lexema, LexicalTable().lexical_table[lexema], position)
                        except Exception as e:
                            token = Token(lexema, Category.ID, position)
                        self.ncolumn += 1
                        return token
                else:
                    self.ncolumn += 1

            elif self.line[i] == '\t':
                self.ncolumn += 3

            elif self.line[i] == "\n":
                self.ncolumn = 0
                self.nline += 1
                self.line = linecache.getline(self.file, self.nline)
                return self.nextToken()

            else:
                token = Token(lexema, Category.UNKNOWN, position)
                self.ncolumn += 1
                return token
