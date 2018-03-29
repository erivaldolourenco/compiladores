# -*- coding: utf-8 -*-
import sys
from lexical import lexicalanalyzer


file = sys.argv[2]
op = sys.argv[1]

if op == "-l":

    lex = lexicalanalyzer.Lexeme(file)
    while lex.isToken():
        lex.nextToken().printToken()

elif op == "-s":
    print("==================== Analisador Sitantico =======================")
else:
    print("======================== Opcao Invalida! ========================")
