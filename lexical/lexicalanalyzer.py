# -*- coding: utf-8 -*-
from token import Token
from category_token import Category

position = [0, 0]


class Lexeme(object):

    def __init__(self, file):
        self.file = file

    def nextToken(self):
        with open(self.file) as file:
            filelines = file.readlines()
            line = filelines[position[0]]
            # print(list(line))
            cont = True
            lexema = ''
            while cont:

                for i in range(position[1], int(line.__len__())):
                    if(line[i] != ' '):
                        lexema += line[i]
                    if line[i].isalnum():
                        if(Category.isSpecial(line[i + 1])):
                            atual_postion = [position[0], position[1]]
                            token = Token(lexema, Category.getCategory(
                                lexema), atual_postion)
                            position[1] += 1
                            cont = False
                            lexeme = ''
                            return token
                        else:
                            position[1] += 1

                    elif line[i] == ' ':
                        position[1] += 1

                    elif line[i] == '(':
                        atual_postion = [position[0], position[1]]
                        token = Token(lexema, Category.getCategory(
                            lexema), atual_postion)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == ')':
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == '{':
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == '}':
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == '[':
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == ']':
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == '+':
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == '-':
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == '*':
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == '/':
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token
                    elif line[i] == '>':
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == '<':
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == '!':
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == ';':
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == '=':
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == ',':
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == "'":
                        token = Token(
                            lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == '\t':
                        position[1] += 3

                    elif line[i] == "\n":
                        position[1] = 0  # zera coluna
                        position[0] += 1  # incrementa linha
                        lexema = ''  # zera  lexema
                        line = filelines[position[0]]
                        break

                    else:
                        # print("DESCONHECIDO")
                        lexema += line[i]
                        token = Token(lexema, Category.UNKNOWN, position)
                        cont = False
                        lexema = ''
                        position[1] += 1

    def isToken(self):
        with open(self.file) as file:
            filelines = file.readlines()
            print(
                "------------------------------------------------------------------------")
            #print("linha Atual:"+str(position[0])+" - Coluna Atual:"+str(position[1]))
            #print("ultima linha arquivo:"+str(filelines.__len__())+" - Ultimo Caracter:"+str(filelines[-1].__len__()))
            # print("------------------------------------------------------------------------")

            if(position[0] == (filelines.__len__() - 1) and position[1] == filelines[-1].__len__()):
                print(
                    '======================= Lista de tokens concluida!! =======================')
                return False
            else:
                return True

    def analise(self):
        while self.isToken():
            return self.nextToken()
