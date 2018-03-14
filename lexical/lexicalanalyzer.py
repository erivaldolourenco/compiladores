# -*- coding: utf-8 -*-
import re
from token import Token
from category_token import Category

position = [0, 0]


class Lexeme(object):

    def __init__(self, file):
        self.file = file

    def nextToken(self):
        print("CHAMANDO NEXTOKEN")
        with open(self.file) as file:

            filelines = file.readlines()
            line = filelines[position[0]]
            print(line)
            col = 0
            lexema = ''
            cont = True
            while cont:
                print("POSITION whilw->"+str(position[1]))
                for i in range(position[0], int(line.__len__())):
                    print("CARACTER -->" + line[i] + "<--")
                    # for line[i] in list(line):
                    if line[i].isalnum():
                        print("ALFANUMERICO")
                        lexema += line[i]
                        if(line[i + 1] == ' ' or line[i + 1] == '\n' ):
                            token = Token(lexema, Category.getCategory(lexema), position)
                            position[1] = col+1
                            cont = False
                            return token
                        else:
                            col += 1

                    elif line[i] == ' ':
                        print("CARACTER VAZIO")
                        col += 1

                    elif line[i] == '(':
                        print("ABRE PAR")
                        col += 1
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        lexema = ''
                        position[1] = col
                        return token

                    elif line[i] == ')':
                        print("FECHA PAR")
                        lexema += line[i]
                        col += 1
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        lexema = ''
                        position[1] = col
                        return token
                    elif line[i] == '{':
                        print("ABRE CHA")
                        lexema += line[i]
                        col += 1
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        lexema = ''
                        position[1] = col
                        return token
                    elif line[i] == '}':
                        print("FECHA PAR")
                        lexema += line[i]
                        col += 1
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        lexema = ''
                        position[1] = col
                        return token
                    elif line[i] == '+':
                        print("MAIS")
                        lexema += line[i]
                        col += 1
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        lexema = ''
                        position[1] = col
                        return token
                    elif line[i] == "\n":
                        print("FIN DE LINHA")
                        position[0] = 0
                        lexema = ''
                        position[0] += 1
                        print("POSITION fim de linha ->"+str(position[0]))
                        line = filelines[position[0]]
                        break

                    elif line[i] == '\t':
                        print("TABULACAO")
                        col += 1
                    else:
                        print("DESCONHECIDO")
                        lexema += line[i]
                        lexema = ''
                        col += 1

    def isToken(self):
        with open(self.file) as file:
            filelines = file.readlines()
            print("linha Atual:"+str(position[0])+" - Coluna Atual:"+str(position[1]))
            print("ultima linha arquivo:"+str(filelines.__len__())+" - Ultimo Caracter:"+str(filelines[-1].__len__()))

            if(position[0] == filelines.__len__() and position[1] == filelines[-1].__len__()):

                return False
            else:
                return True

    def analise(self):
        while self.isToken():
            self.nextToken().printToken()

