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
        print("ERRO")
        print(self.token.printToken())
        exit()

    def printToken(self):
        print(self.token.printToken())

    def programa(self):
        print("           Programa = Funcao Begin")
        self.funcao()
        self.begin()
        print("It´s work!!!")
        # verificar se esta lendo um self.token ou se eh None

    def funcao(self):

        if (self.token.category == Category.FUNCTION):
            print("           Funcao = 'function' Vector Tipo NomeVar 'abrPar' Lparam 'fecPar' Escopo'")

            self.printToken()
            self.token = self.lex.nextToken()

            self.vector()

            if self.tipo() == 1:
                self.erro()

            self.nomeVar()

            if self.token.category == Category.ABR_PAR:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                    self.erro()

            self.l_param()

            if self.token.category == Category.FEC_PAR:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

            self.escopo()

        else:
            print("           Funcao = épsilon")

    def begin(self):
        print("           Begin = 'void' 'begin' 'abrpar' Lparam 'fecpar' Escopo")

        if self.token.category == Category.VOID:
            self.printToken()
            self.token = self.lex.nextToken()

            if self.token.category == Category.BEGIN:
                self.printToken()
                self.token = self.lex.nextToken()

                if self.token.category == Category.ABR_PAR:
                    self.printToken()
                    self.token = self.lex.nextToken()

                    if self.token.category == Category.FEC_PAR:
                        self.printToken()
                        self.token = self.lex.nextToken()
                        self.escopo()

                    else:
                        self.erro()
                else:
                    self.erro()
            else:
                self.erro()
        else:
            self.erro()

    def nomeVar(self):
        print("           NomeVar = 'id' VectorF")
        if self.token.category == Category.ID:
            self.printToken()
            self.token = self.lex.nextToken()
            self.vector_f()
        else:
            self.erro()

    def vector(self):
        if self.token.category == Category.VECTOR:
            print("           Vector = 'vector' Vectorf")
            self.printToken()
            self.token = self.lex.nextToken()
            self.vector_f()
        else:
            print("           Vector = épsilon")
            return 1

    def vector_f(self):
        if self.token.category == Category.ABR_COC:
            
            self.printToken()
            self.token = self.lex.nextToken()
            self.e()

            if self.token.category == Category.FEC_COC:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()



        else:
            #printvazio
            return 1



    def l_param(self):

        self.vector()
        self.tipo()
        self.nomeVar()
        self.l_paramf()

    def l_paramf(self):
        if self.token.category == Category.SEP_VIRG:
            self.printToken()
            self.token = self.lex.nextToken()
            self.l_param()

        else:
            pass
            #print vazio

    def tipo(self):

        if self.token.category == Category.INT:
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.FLOAT:
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.BOOL:
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.CHAR:
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.CCHAR:
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.VOID:
            self.printToken()
            self.token = self.lex.nextToken()

        else:
            return 1
        
    def escopo(self):
        if self.token.category == Category.ABR_CH:
            self.printToken()
            self.token = self.lex.nextToken()
        else:
            self.erro()

        self.comandos()

        if self.token.category == Category.FEC_CH:
            self.printToken()
            self.token = self.lex.nextToken()

        else:
            self.erro()

    def comandos(self):
        if self.cmd() == 1:
            #print vazio
            pass

        else:
            self.comandos()


    def cmd(self):
        if self.token.category == Category.READ:
            self.read()

        elif self.token.category == Category.PUT:
            self.put()

        elif self.token.category == Category.WHILE:
            self._while()

        elif self.token.category == Category.IF:
            self._if()

        elif self.token.category == Category.FOR:
            self._for()

        elif self.token.category == Category.ID:
            self.printToken()
            self.token = self.lex.nextToken()
            self.cmd_f()

            if self.token.category == Category.SEP_P_VIRG:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()


        elif self.token.category == Category.VECTOR:
            self.vectorDecl()
            if self.token.category == Category.SEP_P_VIRG:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

        elif self.tipo() != 1:
            self.decl()

            if self.token.category == Category.SEP_P_VIRG:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

        elif self.token.category == Category.BREAK:
            self.printToken()
            self.token = self.lex.nextToken()

            if self.token.category == Category.SEP_P_VIRG:
                self.printToken()
                self.token = self.lex.nextToken()

            else:
                self.erro()

        elif self.token.category == Category.RETURN:
            self.printToken()
            self.token = self.lex.nextToken()

            self.e()

            if self.token.category == Category.SEP_P_VIRG:
                self.printToken()
                self.token = self.lex.nextToken()

            else:
                self.erro()





        else:
            return 1


    def vectorDecl(self):
        if self.token.category == Category.VECTOR:
            self.printToken()
            self.token = self.lex.nextToken()

            if self.tipo() == 1:
                self.erro()
            else:
                self.nomeVar()
                self.atb_decl()
                #self.decl_f()
        else:
            self.erro()

    def decl(self):
        self.nomeVar()
        self.atb_decl()

    def chamada_func(self):

        if self.token.category == Category.ABR_PAR:
            self.printToken()
            self.token = self.lex.nextToken()
        else:
            self.erro()

        self.l_chamada()

        if self.token.category == Category.FEC_PAR:
            self.printToken()
            self.token = self.lex.nextToken()
        else:
            self.erro()

    def l_chamada(self):
        self.e()
        self.l_chamadaf()

    def l_chamadaf(self):

        if self.token.category == Category.SEP_VIRG:
            self.token = self.lex.nextToken()
            self.e()
            self.l_chamadaf()
        else:
            pass

    def atb_decl(self):

        if self.token.category == Category.ATRIBUICAO:
            self.printToken()
            self.token = self.lex.nextToken()
            self.e()

        else:
            #print("EPSILON")
            pass

    def read(self):
        if self.token.category == Category.READ:
            self.printToken()
            self.token = self.lex.nextToken()

            if self.token.category == Category.ABR_PAR:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

            if self.token.category == Category.SIMPLE_ASP:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

            if self.token.category == Category.CAD_CARACTER:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

            if self.token.category == Category.SIMPLE_ASP:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

            if self.token.category == Category.FEC_PAR:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

            if self.token.category == Category.SEP_P_VIRG:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

        else:
            self.erro()


    def put(self):
        if self.token.category == Category.PUT:
            self.printToken()
            self.token = self.lex.nextToken()


            if self.token.category == Category.ABR_PAR:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

            if self.token.category == Category.SIMPLE_ASP:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()



            if self.token.category == Category.CAD_CARACTER:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

            if self.token.category == Category.SIMPLE_ASP:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

            if self.token.category == Category.FEC_PAR:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

            if self.token.category == Category.SEP_P_VIRG:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

        else:
            self.erro()


    def cmd_f(self):
        if self.token.category == Category.ABR_PAR:
            self.chamada_func()

        elif self.token.category == Category.ABR_COC:
            self.printToken()
            self.token = self.lex.nextToken()


            self.e()

            if self.token.category == Category.FEC_COC:
                self.printToken()
                self.token = self.lex.nextToken()
                self.atribuicao()

            else:
                self.erro()

        elif self.token.category == Category.ATRIBUICAO:
            self.atribuicao()



    def atribuicao(self):
        if self.token.category == Category.ATRIBUICAO:
            self.printToken()
            self.token = self.lex.nextToken()
            self.e()
        else:
            self.erro()




    def _while(self):

        if self.token.category == Category.WHILE:
            self.printToken()
            self.token = self.lex.nextToken()
        else:
            print("while esperado")

        if self.token.category == Category.ABR_PAR:
            self.printToken()
            self.token = self.lex.nextToken()
        else:
            print("ABRPAR esperado")

        self.e()

        if self.token.category == Category.FEC_PAR:
            self.printToken()
            self.token = self.lex.nextToken()
        else:
            print("FECPAR esperado")

        self.escopo()

    def _if(self):

        if self.token.category == Category.IF:
            self.printToken()
            self.token = self.lex.nextToken()
        else:
            print("if esperado")

        if self.token.category == Category.ABR_PAR:
            self.printToken()
            self.token = self.lex.nextToken()
        else:
            print("ABRPAR esperado")

        if self.token.category == Category.FEC_PAR:
            self.printToken()
            self.token = self.lex.nextToken()
        else:
            print("FECPAR esperado")

        self.escopo()
        self._else()

    def _else(self):

        if self.token.category == Category.ELSE:
            self.printToken()
            self.token = self.lex.nextToken()
        else:
            print("ELSE esperado")

        self.escopo()

    def _for(self):
        if self.token.category == Category.FOR:
            self.printToken()
            self.token = self.lex.nextToken()


            if self.token.category == Category.ABR_PAR:
                self.printToken()
                self.token = self.lex.nextToken()
                self.nomeVar()

            else:
                self.erro()

            if self.token.category == Category.IN:
                self.printToken()
                self.token = self.lex.nextToken()
                self.e()

                if self.token.category == Category.TO:
                    self.printToken()
                    self.token = self.lex.nextToken()
                    self.e()

                    if self.token.category == Category.DO:
                        self.printToken()
                        self.token = self.lex.nextToken()

                        if self.token.category == Category.FEC_PAR:
                            self.printToken()
                            self.token = self.lex.nextToken()
                            self.escopo()


                        else:
                            self.erro()

                    else:
                        self.erro()

                else:
                    self.erro()
            else:
                self.erro()


        else:
            self.erro()


    def e(self):
        self.eb()
        self.ebr()

    def eb(self):
        self.tb()
        self.ebr()

    def ebr(self):
        if self.token.category == Category.OP_OR:
            self.tb()
            self.tbr()

        else:
            pass


    def tb(self):
        self.fb()
        self.tbr()

    def tbr(self):
        if self.token.category == Category.OP_AND:
            self.printToken()
            self.token = self.lex.nextToken()
            self.fb()
            self.tbr()

        else:
            pass

    def fb(self):
        if self.token.category == Category.OP_NOT:
            self.printToken()
            self.token = self.lex.nextToken()
            self.relUm()

        else:
            self.relUm()

    def relUm(self):
        self.relDois()
        self.relUmf()

    def relUmf(self):
        if self.token.category == Category.OP_MA:
            self.printToken()
            self.token = self.lex.nextToken()
            self.relDois()

        elif self.token.category == Category.OP_ME:
            self.printToken()
            self.token = self.lex.nextToken()
            self.relDois()

        elif self.token.category == Category.OP_MAIGU:
            self.printToken()
            self.token = self.lex.nextToken()
            self.relDois()

        elif self.token.category == Category.OP_MEIGU:
            self.printToken()
            self.token = self.lex.nextToken()
            self.relDois()

        else:
            pass

    def relDois(self):
        self.concat()
        self.relDoisF()

    def relDoisF(self):
        if self.token.category == Category.OP_MAIGU:
            self.printToken()
            self.token = self.lex.nextToken()
            self.concat()

        else:
            pass

    def concat(self):
        self.ea()
        self.concatr()

    def concatr(self):
        if self.token.category == Category.OP_CONC:
            self.printToken()
            self.token = self.lex.nextToken()
            self.ea()
            self.concatr()
        else:
            pass

    def ea(self):
        self.ta()
        self.ear()

    def ear(self):
        if self.opa() == 1:
            pass
        else:
            self.ta()
            self.ear()

    def opa(self):
        if self.token.category == Category.OP_ADD:
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.OP_SUB:
            self.printToken()
            self.token = self.lex.nextToken()

        else :
            return 1

    def ta(self):
        self.unario()
        self.tar()

    def tar(self):
        if self.opm() == 0:
            self.unario()
            self.tar()
        else:
            pass

    def unario(self):
        if self.token.category == Category.OP_UNA:
            self.printToken()
            self.token = self.lex.nextToken()
            self.fa()

        else:
            self.fa()

    def opm(self):
        if self.token.category == Category.OP_MULT:
            self.printToken()
            self.token = self.lex.nextToken()
            return 0

        elif self.token.category == Category.OP_DIV:
            self.printToken()
            self.token = self.lex.nextToken()
            return 0

        elif self.token.category == Category.OP_MULT:
            self.printToken()
            self.token = self.lex.nextToken()
            return 0

        else:
            return 1

    def fa(self):
        if self.token.category == Category.CONST_INT:
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.CONST_FLO:
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.CONST_CHA:
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.CONST_CCHAR:
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.TRUE:
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.FALSE:
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.ID:
            self.printToken()
            self.token = self.lex.nextToken()
            self.far()

    def far(self):
        if self.token.category == Category.ABR_PAR:
            self.chamada_func()

        else:
            self.vector_f()




















