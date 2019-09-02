import sys
from lexical.lexical_analyzer import Lexeme
from enum import Enum



def erro():
    print("deu merda")

def programa():
    funcao()
    begin()

def funcao():
    if (token == 'FUNCTION'):
        token = lex.nextToken()

    else:
        print('ERRO: FUNCTION ESPERADO')
        erro()

    tipo()
    Array()

    if token == 'id':
        token = lex.nextToken()
        if token == 'ABRPAR':
            token = lex.nextToken();
        else:
            print("ABRPAR esperado")
            erro()
    else:
        print("id esperado")
        erro()

    Lparam()

    if token == 'FECPAR':
        token = lex.nextToken()
    else:
        print("FECPAR esperado")
        erro()

    Escopo()
    funcao()

def begin():
    if token == 'void':
        token = lex.nextToken()

        if token == 'begin':
            token = lex.nextToken()
        else:
            print("begin esperado")
            erro()

    else:
        print("Void esperado")
        erro()

    parametros()
    escopo()


def tipo():
    if token == 'INT':
        token = lex.nextToken()

    elif token == 'FLOAT':
        token = lex.nextToken()

    elif token == 'BOOL':
        token = lex.nextToken()

    elif token == 'CHAR':
        token = lex.nextToken()

    elif token == 'CCHAR':
        token = lex.nextToken()

    elif token == 'VOID':
        token = lex.nextToken()

    else:
        print("Esperado 'int' ou 'float' ou 'bool' ou 'char' ou 'cchar' ou 'void")
        erro()


def array():
    if token == abrcoc:
        token = lex.nextToken
    else:
        print("abrcoc esperado")
        erro()
    arrayf()

def arrayf():
    print('FALTA FAZER')

def nomeVar():
    if token == 'ID':
        token = lex.nextToken
    else:
        print("Id esperado")
        erro()

    array()

def lparam():
    tipo()
    if token == 'ID':
        token = lex.nextToken
    else:
        print("Id esperado")
        erro()
    array()
    lparamf()

def lparamf():
    if token == "SEPVIRG":
        token = lex.nextToken
    else:
        print("SEPVIRG Esperado")


    tipo()
    nomeVar()
    lparamf()

def chamadaFunc():
    if token == 'ABRPAR':
        token = lex.nextToken();
    else:
        print("ABRPAR esperado")

    lChamada()

    if token == 'FECPAR':
        token = lex.nextToken()
    else:
        print("FECPAR esperado")

def lChamada():
    e()
    lChamadaF()

def lChamadaF():
    if token == "SEPVIRG":
        token = lex.nextToken
    else:
        print("SEPVIRG Esperado")

    e()
    lChamadaF()

def escopo():
    if token == 'ABRCH':
        token = lex.nextToken();
    else:
        print("ABRCH esperado")

    comandos()
    if token == 'FECCH':
        token = lex.nextToken()
    else:
        print("FECCH esperado")

def decl():
    tipo()
    nomeVar()
    atbDecl()
    declF()

def DeclF():
    if token == "SEPVIRG":
        token = lex.nextToken
    else:
        print("SEPVIRG Esperado")

    nomeVar()
    atbDecl()
    declF()

def atbDecl():
    if token == 'ATRIBUICAO':
        token = lex.nextToken
    else:
        print("Atribuicao esperado")

    e()

def read():
    print("Não implementado ainda")

def put():
    print("Não implementado ainda")

def comandos():
    cmd()
    comandos()

def cmd():
    print("Falta implementar")

def cmdF():
    print("Falta implementar")

def atribuicao():
    if token == 'ATRIBUICAO':
        token = lex.nextToken
    else:
        print("Atribuicao esperado")
    e()

def wHile():
    if token == 'WHILE':
        token = lex.nextToken
    else:
        print("While esperado")

    if token == 'ABRPAR':
        token = lex.nextToken();
    else:
        print("ABRPAR esperado")

    e()

    if token == 'FECPAR':
        token = lex.nextToken();
    else:
        print("FECPAR esperado")

    escopo()

def iF():
    if token == 'IF':
        token = lex.nextToken
    else:
        print("if esperado")

    if token == 'ABRPAR':
        token = lex.nextToken
    else:
        print("ABRPAR esperado")

    e()

    if token == 'FECPAR':
        token = lex.nextToken
    else:
        print("FECPAR esperado")

    escopo()
    eLse()

def eLse():
    if token == 'ELSE':
        token = lex.nextToken
    else:
        print("ELSE esperado")

    escopo()

def fOr():
    if token == 'FOR':
        token = lex.nextToken
    else:
        print("FOR esperado")

    nomeVar()

    if token == 'IN':
        token = lex.nextToken
    else:
        print("in esperado")

    e()

    if token == 'TO':
        token = lex.nextToken
    else:
        print("TO esperado")

    e()
    escopo()


def e():
    eb()
    ebr()

def eb():
    tb()
    ebr()

def ebr():
    if token == 'opOr':
        token = lex.nextToken
    else
        print("OR esperado")
    tb()
    ebr()

def tb():
    fb()
    tbr()

def tbr():
    if token == 'opAnd':
        token = lex.nextToken
    else
        print("AND esperado")

    fb()
    tbr()

def ea













