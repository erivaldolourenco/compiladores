# -*- coding: utf-8 -*-
import sys
from lexical import lexicalanalyzer


file = sys.argv[2]
op = sys.argv[1]

if op == "-l":
    print("======================= Analisador Lexico =======================")
    while lexicalanalyzer.Lexeme(file).isToken():
    	lexicalanalyzer.Lexeme(file).nextToken().printToken()

elif op == "-s":
    print("======================= Analisador Sitantico =======================")
else:
    print("======================= Opcao Invalida! =======================")
