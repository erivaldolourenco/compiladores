# -*- coding: utf-8 -*-
import sys
from lexical.lexical_analyzer import Lexeme


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
else:
    print("======================== Opcao Invalida! ========================")

# if __name__ == '__main__':
#     print("teste")