# -*- coding: utf-8 -*-
import sys
from lexical.lexical_analyzer import Lexeme
from sintatico.sintatico_analyzer import Sintatico   


file = sys.argv[2]
op = sys.argv[1]

if op == "-l":
    print("INCIANDO...")
    print("=====================================")
    lex = Lexeme(file)

    token = lex.nextToken()

    while token:
        token.printToken()
        token = lex.nextToken()
        # print lex.nextToken().lexeme
        # token.lexeme

    print("=====================================")
    print("CONCLUIDO!")

    
elif op == "-s":
    print("==================== Analisador Sitantico =======================")
    lex = Lexeme(file)
    token = lex.nextToken()
    Sintatico(token,lex).programa()
    print("============================= Fim ===============================")


else:
    print("======================== Opcao Invalida! ========================")

# if __name__ == '__main__':
#     print("teste")