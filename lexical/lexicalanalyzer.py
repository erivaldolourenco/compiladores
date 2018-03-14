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
            # print(list(line))
            # print("Linha = "+str(position[0])+" Coluna = "+str(position[1]))
            cont = True
            lexema = ''
            while cont:
                

                for i in range(position[1], int(line.__len__())):
                    #print("POSITION COLUNA -->"+str(position[1]))
                    #print("LEXEMA -->" + lexema + "<--")
                    # for line[i] in list(line):
                    #print("linha = "+str(position[0])+" coluna = "+str(position[1])+" | i = "+str(i)+ " | caracter = "+line[i] )
                    if(line[i] != ' '):
                        lexema += line[i]
                        #print("LEXEMA = "+lexema)
                    if line[i].isalnum():
                        #print("ALFANUMERICO")
                        
                        if(Category.isSpecial(line[i+1])):
                            #print ("POSITION - " + str(position[1]))
                            #print("CARACTER"+line[i+1])
                            atual_postion = [position[0],position[1]]
                            token = Token(lexema, Category.getCategory(lexema), atual_postion)
                            position[1] += 1
                            cont = False
                            lexeme = ''
                            return token
                        else:
                            position[1] += 1
                            

                    elif line[i] == ' ':
                        #print("CARACTER VAZIO")
                        position[1] += 1


                    elif line[i] == '(':
                        # lexema = line[i]
                        #print("ABRE PAR | lexema ="+ lexema)
                        atual_postion = [position[0],position[1]]
                        token = Token(lexema, Category.getCategory(lexema), atual_postion)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == ')':
                        #print("FECHA PAR")
                        token = Token(lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == '{':
                        #print("ABRE CHA")
                        token = Token(lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == '}':
                        #print("FECHA PAR")
                        token = Token(lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token

                    elif line[i] == '+':
                        #print("MAIS")
                        token = Token(lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token
                    elif line[i] == ';':
                        #print("MAIS")
                        token = Token(lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token
                    elif line[i] == '=':
                        #print("MAIS")
                        token = Token(lexema, Category.getCategory(lexema), position)
                        cont = False
                        lexema = ''
                        position[1] += 1
                        return token
                    
                    elif line[i] == '\xe2' and line[i+1] =='\x80' and line[i+2] == '\x98':
                        #print("ASPAS SIMPLES")
                        lexeme = '\xe2\x80\x98'
                        token = Token(lexema, Category.UNKNOWN, position)
                        position[1] += 2

                    elif line[i] == '\t':
                        #print("TABULACAO")
                        position[1] += 1

                    elif line[i] == "\n":
                       # print("FIN DE LINHA")
                        position[1] = 0 #zera coluna
                        position[0] += 1 #incrementa linha
                        lexema = '' # zera  lexema
                        #print("POSITION fim de linha ->"+str(position[0]))
                        line = filelines[position[0]]
                        break

                    else:
                        #print("DESCONHECIDO")
                        lexema += line[i]
                        token = Token(lexema, Category.UNKNOWN, position)
                        cont = False
                        lexema = ''
                        position[1] += 1

    def isToken(self):
        with open(self.file) as file:
            filelines = file.readlines()
            print("------------------------------------------------------------------------")
            #print("linha Atual:"+str(position[0])+" - Coluna Atual:"+str(position[1]))
            #print("ultima linha arquivo:"+str(filelines.__len__())+" - Ultimo Caracter:"+str(filelines[-1].__len__()))
            #print("------------------------------------------------------------------------")

            if(position[0] == filelines.__len__() and position[1] == filelines[-1].__len__()):

                return False
            else:
                return True

    def analise(self):
        while self.isToken():
            self.nextToken().printToken()

