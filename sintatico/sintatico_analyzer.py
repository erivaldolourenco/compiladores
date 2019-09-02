# -*- coding: utf-8 -*-
import sys
from lexical.lexical_analyzer import Lexeme
from lexical.category_token import Category

from enum import Enum


class Sintatico(object):

    def __init__(self,token,lex):
        self.token = token
        self.lex = lex
    

    def erro(self):
        print("deu merda")

    def programa(self):
        self.funcao()
        # self.begin()
        # verificar se esta lendo um token ou se eh None

    def funcao(self):

        if (self.token.category == Category.FUNCTION):
            self.token = self.lex.nextToken()
        else:
            print('ERRO: FUNCTION ESPERADO')
            self.erro()
        self.tipo()
        self.array()

        if self.token.category == Category.ID:
            self.token = self.lex.nextToken()
            
            if self.token.category == Category.ABR_PAR:
                self.token = self.lex.nextToken()
            else:
                print("ABRPAR esperado")
                self.erro()
        else:
            print("id esperado")
            self.erro()

        self.Lparam()

        if self.token.category == Category.FEC_PAR:
            self.token = self.lex.nextToken()
        else:
            print("FECPAR esperado")
            self.erro()

        self.Escopo()
        self.funcao()

    def begin(self):
        if self.token == Category.VOID:
            self.token = self.lex.nextToken()

            if self.token == Category.BEGIN:
                self.token = self.lex.nextToken()
            else:
                print("begin esperado")
                self.erro()

        else:
            print("Void esperado")
            self.erro()

        self.parametros()
        self.escopo()


    def tipo(self):
        if self.token.category == Category.INT:
            self.token = self.lex.nextToken()

        elif self.token == Category.FLOAT:
            self.token = self.lex.nextToken()

        elif self.token == Category.BOOL:
            self.token = self.lex.nextToken()

        elif self.token == Category.CHAR:
            self.token = self.lex.nextToken()

        elif self.token == Category.CCHAR:
            self.token = self.lex.nextToken()

        elif self.token == Category.VOID:
            self.token = self.lex.nextToken()

        else:
            print("Esperado 'int' ou 'float' ou 'bool' ou 'char' ou 'cchar' ou 'void")
            self.erro()


    def array(self):
        if self.token.category == Category.ABR_COC:
            self.token = self.lex.nextToken()
        else:
            print("abrcoc esperado")
            self.erro()
        self.arrayf()

    def arrayf(self):
        print('FALTA FAZER')

    def nomeVar(self):
        if token == 'ID':
            token = lex.nextToken
        else:
            print("Id esperado")
            erro()

        array()

    def lparam(self):
        tipo()
        if token == 'ID':
            token = lex.nextToken
        else:
            print("Id esperado")
            erro()
        array()
        lparamf()

    def lparamf(self):
        if token == "SEPVIRG":
            token = lex.nextToken
        else:
            print("SEPVIRG Esperado")


        tipo()
        nomeVar()
        lparamf()

    def chamadaFunc(self):
        if token == 'ABRPAR':
            token = lex.nextToken();
        else:
            print("ABRPAR esperado")

        lChamada()

        if token == 'FECPAR':
            token = lex.nextToken()
        else:
            print("FECPAR esperado")

    def lChamada(self):
        e()
        lChamadaF()

    def lChamadaF(self):
        if token == "SEPVIRG":
            token = lex.nextToken
        else:
            print("SEPVIRG Esperado")

        e()
        lChamadaF()

    def escopo(self):
        if token == 'ABRCH':
            token = lex.nextToken();
        else:
            print("ABRCH esperado")

        comandos()
        if token == 'FECCH':
            token = lex.nextToken()
        else:
            print("FECCH esperado")

    def decl(self):
        tipo()
        nomeVar()
        atbDecl()
        declF()

    def DeclF(self):
        if token == "SEPVIRG":
            token = lex.nextToken
        else:
            print("SEPVIRG Esperado")

        nomeVar()
        atbDecl()
        declF()

    def atbDecl(self):
        if token == 'ATRIBUICAO':
            token = lex.nextToken
        else:
            print("Atribuicao esperado")

        e()

    def read(self):
        print("Não implementado ainda")

    def put():
        print("Não implementado ainda")

    def comandos(self):
        cmd()
        comandos()

    def cmd(self):
        print("Falta implementar")

    def cmdF(self):
        print("Falta implementar")

    def atribuicao(self):
        if token == 'ATRIBUICAO':
            token = lex.nextToken
        else:
            print("Atribuicao esperado")
        e()

    def wHile(self):
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

    def iF(self):
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

    def eLse(self):
        if token == 'ELSE':
            token = lex.nextToken
        else:
            print("ELSE esperado")

        escopo()

    def f_for(self):
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


    def e(self):
        eb()
        ebr()

    def eb(self):
        tb()
        ebr()

    def ebr(self):
        if token == 'opOr':
            token = lex.nextToken
        else:
            print("OR esperado")
        tb()
        ebr()

    def tb(self):
        fb()
        tbr()

    def tbr(self):
        if token == 'opAnd':
            token = lex.nextToken
        else:
            print("AND esperado")

        fb()
        tbr()

    # def ea