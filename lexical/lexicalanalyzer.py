# -*- coding: utf-8 -*-
import re
from token import Token

class Lexeme(object):

    def __init__(self, file):
        self.file = file

    def analizer(self):
        li = 0
        col = 0
        with open(self.file) as file:
            filelines = file.readlines()
            # print(filelines)
            for line in filelines:
                li += 1
                lexema = ''
                for caracter in list(line):
                    if re.findall('[^A-Za-z0-9]', caracter):
                        if caracter == ' ':
                            if lexema.__len__() == 0:
                                col += 1
                                lexema == ''
                            else:
                                col += 1
                                lexema == ''

                        elif caracter == '(':
                            col += 1
                            lexema = ''
                        elif caracter == ')':
                            lexema += caracter
                            col += 1
                            lexema = ''
                        elif caracter == '\n':
                            col += 1
                            lexema = ''
                        elif caracter == '\t':
                            col += 1
                        else:
                            lexema += caracter
                            lexema = ''
                            col += 1
                    else:
                        lexema += caracter
                        col += 1


    
    def nextToken(self):
        pass