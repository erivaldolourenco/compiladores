# -*- coding: utf-8 -*-
import re
class Lexeme(object):

    def __init__(self, file):
        self.file = file

    def analizer(self):
    	li = 0
    	col = 0
    	list_of_lexema = []
        with open(self.file) as file:
            filelines = file.readlines()
            # print(filelines)
            for line in filelines:
            	list_of_lexema = []
            	li += 1
            	lexema = ''
            	# print("LINHA"+str(li)+": "+ line)
            	# list_of_lexema.append(lexema)

            	for caracter in list(line):
            		# print("--"+caracter+"--")
            		if re.findall('[^A-Za-z0-9]',caracter):
            			# print("CARACTER ESPECIAL")
            			if caracter == ' ' and lexema.__len__() == 0:
            				col += 1
            				lexema == ''

	            		elif caracter == '(':
	            			list_of_lexema.append(lexema)
	            			
	            			list_of_lexema.append(caracter)
            				col += 1
            				lexema = ''
	            		elif caracter == ')':
	            			lexema += caracter
	            			list_of_lexema.append(lexema)
            				col += 1
            				lexema = ''
	            		elif caracter == '\n':
	            			list_of_lexema.append(lexema)
	            			col += 1
	            			lexema = ''
	            		elif caracter == '\t':
	            			col += 1
	            		else:
	            			lexema += caracter
	            			list_of_lexema.append(lexema)
	            			lexema = ''
            				col += 1
	            	else:
	            		# print("ALFA NUMERICO")
            			lexema += caracter
            			col += 1


           	print(list_of_lexema)
           	



                	# print("->" + caracter)
                	# col += 1

        # print("Linha:"+str(li))
        # print("Coluna"+str(col))