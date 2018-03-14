# -*- coding: utf-8 -*-
import sys
from lexical import lexicalanalyzer


file = sys.argv[2]
op = sys.argv[1]

if op == "-l":
    print("Analizador Lexico")
    lexicalanalyzer.Lexeme(file).analise()

elif op == "-s":
    print("Analizador Sitantico")
else:
    print("Opcao Invalida!")
