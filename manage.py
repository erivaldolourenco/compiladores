# -*- coding: utf-8 -*-
import sys
from lexical.lexical_analyzer import Lexeme
from sintatico.sintatico_analyzer import Sintatico
from tools.tools import Tools


file = sys.argv[2]
op = sys.argv[1]


if op == "-l":
    Tools.print_f("==================== Analisador Lexico =======================",file)
    lex = Lexeme(file)

    token = lex.nextToken()

    while token:
        token.printToken(file)
        token = lex.nextToken()
        # print lex.nextToken().lexeme
        # token.lexeme
    Tools.print_f("\n============================= Fim ===============================", file)

elif op == "-s":
    Tools.print_f("==================== Analisador Sitantico =======================",file)
    lex = Lexeme(file)
    token = lex.nextToken()
    Sintatico(token, lex, file).programa()
    Tools.print_f("============================= Fim ===============================",file)

else:
    print("======================== Opcao Invalida! ========================")

# if __name__ == '__main__':
#     print("teste")
