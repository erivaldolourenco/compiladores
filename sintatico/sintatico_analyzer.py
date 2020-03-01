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
        if self.token.printToken() is not None:
            self.token.printToken()

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
            print("           VectorF = 'abrCoc' e 'fecCoc'")
            self.printToken()
            self.token = self.lex.nextToken()
            self.e()

            if self.token.category == Category.FEC_COC:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()



        else:
            print("           VectorF = épsilon")
            return 1



    def l_param(self):

        print("           Lparam = 'Vector' Tipo NomeVar LparamF")

        self.vector()
        self.tipo()
        self.nomeVar()
        self.l_paramf()

    def l_paramf(self):
        print("           LparamF = 'sepVirg' Lparam")
        if self.token.category == Category.SEP_VIRG:
            self.printToken()
            self.token = self.lex.nextToken()
            self.l_param()

        else:
            self.erro()


    def tipo(self):

        if self.token.category == Category.INT:
            print("           Tipo = 'int'")
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.FLOAT:
            print("           Tipo = 'Float'")
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.BOOL:
            print("           Tipo = 'BOOL")
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.CHAR:
            print("           Tipo = 'char")
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.CCHAR:
            print("           Tipo = 'cchar'")
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.VOID:
            print("           Tipo = 'void")
            self.printToken()
            self.token = self.lex.nextToken()

        else:
            return 1
        
    def escopo(self):
        print("           Escopo = 'abrCh' Comandos 'FecCh")
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
            print("           Comandos = épsilon")

        else:
            print("           Comandos = Cmd Comandos")
            self.comandos()


    def cmd(self):
        if self.token.category == Category.READ:
            print("           Cmd = Read")
            self.read()

        elif self.token.category == Category.PUT:
            print("           Cmd = Put")
            self.put()

        elif self.token.category == Category.WHILE:
            print("           Cmd = While")
            self._while()

        elif self.token.category == Category.IF:
            print("           Cmd = IF")
            self._if()

        elif self.token.category == Category.FOR:
            print("           Cmd = For")
            self._for()

        elif self.token.category == Category.ID:
            print("           Cmd = 'id' CmdF 'sepPtv'")
            self.printToken()
            self.token = self.lex.nextToken()
            self.cmd_f()

            if self.token.category == Category.SEP_P_VIRG:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()


        elif self.token.category == Category.VECTOR:
            print("           Cmd = VectorDecl Tipo Decl")
            self.vectorDecl()
            if self.token.category == Category.SEP_P_VIRG:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

        elif self.tipo() != 1:
            print("           Cmd = Tipo Decl 'SepPtv")
            self.decl()

            if self.token.category == Category.SEP_P_VIRG:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

        elif self.token.category == Category.BREAK:
            print("           Cmd = 'break' 'sepptv'")
            self.printToken()
            self.token = self.lex.nextToken()

            if self.token.category == Category.SEP_P_VIRG:
                self.printToken()
                self.token = self.lex.nextToken()

            else:
                self.erro()

        elif self.token.category == Category.RETURN:
            print("           Cmd = 'return' e 'sepPtv")
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
            print("           VectorDecl = 'vector' Tipo Decl")
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
        print("           Tipo = NomeVar AtbDecl")
        self.nomeVar()
        self.atb_decl()

    def chamada_func(self):
        print("           ChamadaFuncao = 'abrPar' Lchamada 'fecPar'")
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
        print("           Lchamada = e lchamdaf")
        self.e()
        self.l_chamadaf()

    def l_chamadaf(self):

        if self.token.category == Category.SEP_VIRG:
            print("           LchamadaF = 'sepVir' e Lchamda f")
            self.token = self.lex.nextToken()
            self.e()
            self.l_chamadaf()
        else:
            print("           LchamadaF = épsilon")

    def atb_decl(self):

        if self.token.category == Category.ATRIBUICAO:
            print("           AtbDecl = 'atribuicao' e")
            self.printToken()
            self.token = self.lex.nextToken()
            self.e()

        else:
            print("           AtbDecl = épsilon")

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
            print("           CmdF = ChamadaFuncao")
            self.chamada_func()

        elif self.token.category == Category.ABR_COC:
            print("           CmdF = 'abrCoc' e 'fecCoc' Atribuicao")
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
            print("           CmdF = Atribuicao")
            self.atribuicao()



    def atribuicao(self):
        if self.token.category == Category.ATRIBUICAO:
            print("           Atribuicao = 'atribuicao' e")
            self.printToken()
            self.token = self.lex.nextToken()
            self.e()
        else:
            self.erro()




    def _while(self):
        print("           While = 'while' 'abrPar' E 'fecPar' Escopo")
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
        print("           If = 'if' 'abrPar' e 'fecPar' Escopo Else")
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
            print("           Else = 'else' Escopo")
            self.printToken()
            self.token = self.lex.nextToken()
            self.escopo()

        else:
            print("           Else = épsilon")


    def _for(self):
        print("           For = 'for' 'abrPar' NomeVar 'in' E 'to' E 'do' Escopo")
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
        print("           E = Eb Ebr")
        self.eb()
        self.ebr()

    def eb(self):
        print("           Eb = Tb Ebr")
        self.tb()
        self.ebr()

    def ebr(self):
        if self.token.category == Category.OP_OR:
            print("           Ebr = 'opOr' Tb Tbr")
            self.tb()
            self.tbr()

        else:
            print("           Ebr = épsilon")


    def tb(self):
        print("           Tb = Fb Tbr")
        self.fb()
        self.tbr()

    def tbr(self):
        if self.token.category == Category.OP_AND:
            print("           Tbr = 'opAnd' Fb Tbr")
            self.printToken()
            self.token = self.lex.nextToken()
            self.fb()
            self.tbr()

        else:
            print("           Tbr = épsilon")

    def fb(self):
        if self.token.category == Category.OP_NOT:
            print("           Fb = opNot RelUm")
            self.printToken()
            self.token = self.lex.nextToken()
            self.relUm()

        else:
            print("           Fb = RelUm")
            self.relUm()

    def relUm(self):
        print("           RelUm = RelDois RelUmF")
        self.relDois()
        self.relUmf()

    def relUmf(self):
        if self.token.category == Category.OP_MA:
            print("           RelUmF = 'opMa' RelDois")
            self.printToken()
            self.token = self.lex.nextToken()
            self.relDois()

        elif self.token.category == Category.OP_ME:
            print("           RelUmF = 'opMe' RelDois")
            self.printToken()
            self.token = self.lex.nextToken()
            self.relDois()

        elif self.token.category == Category.OP_MAIGU:
            print("           RelUmF = 'opMaigu' RelDois")
            self.printToken()
            self.token = self.lex.nextToken()
            self.relDois()

        elif self.token.category == Category.OP_MEIGU:
            print("           RelUmF = 'opMeigu' RelDois")
            self.printToken()
            self.token = self.lex.nextToken()
            self.relDois()

        else:
            print("           RelUmf = épsilon")

    def relDois(self):
        print("           RelDois = Concat RelDoisF")
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
        print("           Concat = Ea ConcatR")
        self.ea()
        self.concatr()

    def concatr(self):
        if self.token.category == Category.OP_CONC:
            print("           ConcatR = 'opconc' Ea ConcatR")
            self.printToken()
            self.token = self.lex.nextToken()
            self.ea()
            self.concatr()
        else:
            print("           ConcatR = épsilon")

    def ea(self):
        print("           Ea = Ta Ear")
        self.ta()
        self.ear()

    def ear(self):
        if self.opa() == 1:
            print("           Ear = épsilon")
        else:
            print("           Ear = ta Ear")
            self.ta()
            self.ear()

    def opa(self):
        if self.token.category == Category.OP_ADD:
            print("           Opa = 'opAdd'")
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.OP_SUB:
            print("           Opa = 'opSub'")
            self.printToken()
            self.token = self.lex.nextToken()

        else :
            return 1

    def ta(self):
        print("           Ta = Unario Tar")
        self.unario()
        self.tar()

    def tar(self):
        if self.opm() == 0:
            print("           Tar = Opm Unario Tar")
            self.unario()
            self.tar()
        else:
            print("           Tar = épsilon")

    def unario(self):
        if self.token.category == Category.OP_UNA:
            print("           Unario = 'opUna' Fa")
            self.printToken()
            self.token = self.lex.nextToken()
            self.fa()

        else:
            print("           Unario = Fa")
            self.fa()

    def opm(self):
        if self.token.category == Category.OP_MULT:
            print("           Opm = 'opMult'")
            self.printToken()
            self.token = self.lex.nextToken()
            return 0

        elif self.token.category == Category.OP_DIV:
            print("           Opm = 'opDiv'")
            self.printToken()
            self.token = self.lex.nextToken()
            return 0

        elif self.token.category == Category.OP_RET:
            print("           Opm = 'opRet")
            self.printToken()
            self.token = self.lex.nextToken()
            return 0

        else:
            return 1

    def fa(self):
        if self.token.category == Category.CONST_INT:
            print("           Fa = 'constInt'")
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.CONST_FLO:
            print("           Fa = 'constFlo'")
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.CONST_CHA:
            print("           Fa = 'ConstCha'")
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.CONST_CCHAR:
            print("           Fa = 'constCchar'")
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.TRUE:
            print("           Fa = 'True'")
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.FALSE:
            print("           Fa = 'False'")
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.ID:
            print("           Fa = 'Id' Far")
            self.printToken()
            self.token = self.lex.nextToken()
            self.far()

    def far(self):
        if self.token.category == Category.ABR_PAR:
            print("           Far = 'abrPar' ChamadaFuncao")
            self.chamada_func()

        else:
            print("           Far = VectorF")
            self.vector_f()




















