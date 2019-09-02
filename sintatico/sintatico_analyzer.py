# -*- coding: utf-8 -*-
import sys
from lexical.lexical_analyzer import Lexeme
from lexical.category_token import Category

from enum import Enum


class Sintatico(object):

    def __init__(self, token, lex):
        self.token = token
        self.lex = lex
    

    def erro(self):
        print("deu merda")

    def programa(self):
        self.funcao()
        # self.begin()
        # verificar se esta lendo um self.token ou se eh None

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

        self.lparam()

        if self.token.category == Category.FEC_PAR:
            self.token = self.lex.nextToken()
        else:
            print("FECPAR esperado")
            self.erro()

        self.escopo()
        self.funcao()

    def begin(self):
        if self.token.category == Category.VOID:
            self.token = self.lex.nextToken()

            if self.token.category == Category.BEGIN:
                self.token = self.lex.nextToken()
            else:
                print("begin esperado")
                self.erro()

        else:
            print("Void esperado")
            self.erro()

        self.parametros()
        self.escopo()

    def parametros(self):
        pass

    def tipo(self):
        if self.token.category == Category.INT:
            self.token = self.lex.nextToken()

        elif self.token.category == Category.FLOAT:
            self.token = self.lex.nextToken()

        elif self.token.category == Category.BOOL:
            self.token = self.lex.nextToken()

        elif self.token.category == Category.CHAR:
            self.token = self.lex.nextToken()

        elif self.token.category == Category.CCHAR:
            self.token = self.lex.nextToken()

        elif self.token.category == Category.VOID:
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
        if self.token.category == Category.ID:
            self.token = self.lex.nextToken()
        else:
            print("Id esperado")
            self.erro()

        self.array()

    def lparam(self):
        self.tipo()
        if self.token.category == Category.ID :
            self.token = self.lex.nextToken()
        else:
            print("Id esperado")
            self.erro()
        self.array()
        self.lparamf()

    def lparamf(self):
        if self.token.category == Category.SEP_P_VIRG:
            self.token = self.lex.nextToken()
        else:
            print("SEPVIRG Esperado")


        self.tipo()
        self.nomeVar()
        self.lparamf()

    def chamadaFunc(self):
        if self.token.category == 'ABRPAR':
            self.token = self.lex.nextToken()
        else:
            print("ABRPAR esperado")

        self.lChamada()

        if self.token.category == 'FECPAR':
            self.token = self.lex.nextToken()
        else:
            print("FECPAR esperado")

    def lChamada(self):
        self.e()
        self.lChamadaF()

    def lChamadaF(self):
        if self.token.category == "SEPVIRG":
            self.token = self.lex.nextToken()
        else:
            print("SEPVIRG Esperado")

        self.e()
        self.lChamadaF()

    def escopo(self):
        if self.token.category == 'ABRCH':
            self.token = self.lex.nextToken()
        else:
            print("ABRCH esperado")

        self.comandos()
        if self.token.category == 'FECCH':
            self.token = self.lex.nextToken()
        else:
            print("FECCH esperado")

    def decl(self):
        self.tipo()
        self.nomeVar()
        self.atbDecl()
        self.declF()

    def DeclF(self):
        if self.token.category == "SEPVIRG":
            self.token = self.lex.nextToken()
        else:
            print("SEPVIRG Esperado")

        self.nomeVar()
        self.atbDecl()
        self.declF()

    def declF(self):
        pass

    def atbDecl(self):
        if self.token.category == 'ATRIBUICAO':
            self.token = self.lex.nextToken()
        else:
            print("Atribuicao esperado")

        self.e()

    def read(self):
        print("Não implementado ainda")

    def put(self):
        print("Não implementado ainda")

    def comandos(self):
        self.cmd()
        self.comandos()

    def cmd(self):
        print("Falta implementar")

    def cmdF(self):
        print("Falta implementar")

    def atribuicao(self):
        if self.token.category == 'ATRIBUICAO':
            self.token = self.lex.nextToken()
        else:
            print("Atribuicao esperado")
        self.e()

    def wHile(self):
        if self.token.category == 'WHILE':
            self.token = self.lex.nextToken()
        else:
            print("While esperado")

        if self.token.category == 'ABRPAR':
            self.token = self.lex.nextToken()
        else:
            print("ABRPAR esperado")

        self.e()

        if self.token.category == 'FECPAR':
            self.token = self.lex.nextToken()
        else:
            print("FECPAR esperado")

        self.escopo()

    def iF(self):
        if self.token.category == 'IF':
            self.token = self.lex.nextToken()
        else:
            print("if esperado")

        if self.token.category == 'ABRPAR':
            self.token = self.lex.nextToken()
        else:
            print("ABRPAR esperado")

        self.e()

        if self.token.category == 'FECPAR':
            self.token = self.lex.nextToken()
        else:
            print("FECPAR esperado")

        self.escopo()
        self.eLse()

    def eLse(self):
        if self.token.category == 'ELSE':
            self.token = self.lex.nextToken()
        else:
            print("ELSE esperado")

        self.escopo()

    def f_for(self):
        if self.token.category == 'FOR':
            self.token = self.lex.nextToken()
        else:
            print("FOR esperado")

        self.nomeVar()

        if self.token.category == 'IN':
            self.token = self.lex.nextToken()
        else:
            print("in esperado")

        self.e()

        if self.token.category == 'TO':
            self.token = self.lex.nextToken()
        else:
            print("TO esperado")

        self.e()
        self.escopo()


    def e(self):
        self.eb()
        self.ebr()

    def eb(self):
        self.tb()
        self.ebr()

    def ebr(self):
        if self.token.category == 'opOr':
            self.token = self.lex.nextToken()
        else:
            print("OR esperado")
        self.tb()
        self.ebr()

    def tb(self):
        self.fb()
        self.tbr()

    def tbr(self):
        if self.token.category == 'opAnd':
            self.token = self.lex.nextToken()
        else:
            print("AND esperado")

        self.fb()
        self.tbr()

    def fb(self):
        pass