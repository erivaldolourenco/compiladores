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
        print(self.token.printToken())
        exit()

    def programa(self):
        self.funcao()
        self.begin()
        # verificar se esta lendo um self.token ou se eh None

    def funcao(self):

        if (self.token.category == Category.FUNCTION):
            self.token = self.lex.nextToken()
            self.tipo()

            if self.token.category == Category.ID:
                self.token = self.lex.nextToken()
            else:
                print("ERRO: ID ESPERADO")

            if self.token.category == Category.ABR_PAR:
                self.token = self.lex.nextToken()
            else:
                print("ERRO: ABRPAR ESPERADO")

            self.l_param()

            if self.token.category == Category.FEC_PAR:
                self.token = self.lex.nextToken()
            else:
                print("FECPAR ESPERADO")
                self.erro()

            self.escopo()
            self.funcao()
        else:
            print("EPSILON")

    def begin(self):
        if self.token.category == Category.VOID:
            self.token = self.lex.nextToken()
        else:
            print("ERRO: VOID ESPERADO")

        if self.token.category == Category.BEGIN:
            self.token = self.lex.nextToken()
        else:
            print("ERRO: BEGIN ESPERADO")
            self.erro()

        if self.token.category == Category.ABR_PAR:
            self.token = self.lex.nextToken()
        else:
            print("ERRO: ABR_PAR ESPERADO")

        if self.token.category == Category.FEC_PAR:
            self.token = self.lex.nextToken()
        else:
            print("FECPAR esperado")

        self.escopo()

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


    def vector(self):
        if self.token.category == Category.ABR_COC:
            self.token = self.lex.nextToken()
        else:
            print("EPSILON")

        self.vector_f()


    def vector_f(self):
        if self.token.category == Category.FEC_COC:
            self.token = self.lex.nextToken()
        else:
            self.e()
            if self.token.category == Category.ABR_COC:
                self.token = self.lex.nextToken()
            else:
                print("ERRO: FEC_COC ESPERADO")
            
    def nome_var(self):
        if self.token.category == Category.ID:
            self.token = self.lex.nextToken()
        else:
            print("Id esperado")
            self.erro()

        self.array()

    def l_param(self):
        
        if self.token.category == Category.FEC_PAR :
            self.token = self.lex.nextToken()
        else:
            self.tipo()
            if self.token.category == Category.ID :
                self.token = self.lex.nextToken()
                self.l_paramf()
            else:
                print("ERRO: ID ESPERADO")
                self.erro()
        

    def l_paramf(self):

        self.tipo()

        if self.token.category == Category.SEP_P_VIRG:
            self.token = self.lex.nextToken()
        else:
            print("SEPVIRG Esperado")


        
        self.nome_var()
        self.l_paramf()

    def chamada_func(self):

        if self.token.category == Category.ABR_PAR:
            self.token = self.lex.nextToken()
        else:
            print("ABRPAR esperado")

        self.l_chamada()

        if self.token.category == Category.FEC_PAR:
            self.token = self.lex.nextToken()
        else:
            print("FECPAR esperado")

    def l_chamada(self):
        self.e()
        self.l_chamadaf()

    def l_chamadaf(self):

        if self.token.category == Category.SEP_VIRG:
            self.token = self.lex.nextToken()
        else:
            print("SEPVIRG Esperado")

        self.e()
        self.l_chamadaf()

    def escopo(self):
        if self.token.category == Category.ABR_CH:
            self.token = self.lex.nextToken()
        else:
            print("ABRCH esperado")

        self.comandos()
        if self.token.category == Category.FEC_CH:
            self.token = self.lex.nextToken()
        else:
            print("FECCH esperado")

    def decl(self):
        self.tipo()
        self.nome_var()
        self.atb_decl()
        self.decl_f()

    def decl_f(self):

        if self.token.category == Category.SEP_VIRG:
            self.token = self.lex.nextToken()
        else:
            print("SEPVIRG Esperado")

        self.nome_var()
        self.atb_decl()
        self.decl_f()

    def decl_f(self):
        pass

    def atb_decl(self):

        if self.token.category == Category.ATRIBUICAO:
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

    def cmd_f(self):
        print("Falta implementar")

    def atribuicao(self):
        if self.token.category == Category.ATRIBUICAO:
            self.token = self.lex.nextToken()
        else:
            print("Atribuicao esperado")
        self.e()


    def _while(self):
        if self.token.category == Category.WHILE:

            self.token = self.lex.nextToken()
        else:
            print("while esperado")

        if self.token.category == Category.ABR_PAR:
            self.token = self.lex.nextToken()
        else:
            print("ABRPAR esperado")

        self.e()

        if self.token.category == Category.FEC_PAR:
            self.token = self.lex.nextToken()
        else:
            print("FECPAR esperado")

        self.escopo()

    def _if(self):

        if self.token.category == Category.IF:
            self.token = self.lex.nextToken()
        else:
            print("if esperado")

        if self.token.category == Category.ABR_PAR:
            self.token = self.lex.nextToken()
        else:
            print("ABRPAR esperado")

        self.e()

        if self.token.category == Category.FEC_PAR:
            self.token = self.lex.nextToken()
        else:
            print("FECPAR esperado")

        self.escopo()
        self._else()

    def _else(self):

        if self.token.category == Category.ELSE:
            self.token = self.lex.nextToken()
        else:
            print("ELSE esperado")

        self.escopo()

    def _for(self):
        if self.token.category == Category.FOR:

            self.token = self.lex.nextToken()
        else:
            print("FOR esperado")

        self.nome_var()

        # if self.token.category == 'IN':
        #     self.token = self.lex.nextToken()
        # else:
        #     print("in esperado")

        # self.e()

        # if self.token.category == 'TO':
        #     self.token = self.lex.nextToken()
        # else:
        #     print("TO esperado")

        self.e()
        self.escopo()


    def e(self):
        self.eb()
        self.ebr()

    def eb(self):
        self.tb()
        self.ebr()

    def ebr(self):
        if self.token.category == Category.OP_OR:
            self.token = self.lex.nextToken()
        else:
            print("OR esperado")
        self.tb()
        self.ebr()

    def tb(self):
        self.fb()
        self.tbr()

    def tbr(self):
        if self.token.category == Category.OP_AND:
            self.token = self.lex.nextToken()
        else:
            print("AND esperado")

        self.fb()
        self.tbr()

    def ea(self):
        self.ta()
        self.ear()

    def ear(self):
        self.opa()
        self.ta()
        self.ear()

    def ta(self):
        self.eunario()
        self.tar()

    def tar(self):
        self.opm()
        self.eunario()
        tar()

    def eunario(self):
        if self.token.category == Category.OP_NOT:
            self.token = self.lex.nextToken
            self.fa()

        else:
            self.fa()

    def fa(self):
        if self.token.category == Category.ABR_PAR:
            self.token = self.lex.nextToken
            e()
            if self.token.category == Category.FEC_PAR:
                self.token = self.lex.nextToken
            else:
                print("FECPAR ESPERADO")

        elif self.token.category == Category.CONST_INT:
            self.token = self.lex.nextToken
            return

        elif self.token.category == Category.CONST_FLO:
            self.token = self.lex.nextToken
            return

        elif self.token.category == Category.CONST_CHA:
            self.token = self.lex.nextToken
            return

        elif self.token.category == Category.CONST_CCHAR:
            self.token = self.lex.nextToken
            return

        elif self.token.category == Category.TRUE :
            self.token = self.lex.nextToken
            return

        elif self.token.category == Category.FALSE:
            self.token = self.lex.nextToken
            return

        elif self.token.category == Category.ID:
            self.id()
            self.far()


        else:
            print("Erro")

    def far(self):
        self.chamadaFunc()

    def opa(self):
        if self.token.category == Category.OP_ADD:
            self.token = self.lex.nextToken

        elif self.token.category == Category.OP_SUB:
            self.token = self.lex.nextToken

        else:
            print("OPADD ou OPSUB esperado")

    def opm(self):
        if self.token.category == Category.OP_MULT:
            self.token = self.lex.nextToken

        elif self.token.category == Category.OP_DIV:
            tself.token = self.lex.nextToken

        elif self.token.category == Category.OP_RET:
            tself.token = self.lex.nextToken

        else:
            print("OPMULTI OU OPDIV OU OPRET esperado")

    def id(self):
        if self.token.category == Category.ID:
            self.token = self.lex.nextToken
        else:
            print("ID esperado")
            erro()


