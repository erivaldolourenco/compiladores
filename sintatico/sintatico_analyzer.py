# -*- coding: utf-8 -*-
import sys
from lexical.lexical_analyzer import Lexeme
from lexical.category_token import Category
from tools.tools import Tools

from enum import Enum


class Sintatico(object):

    def __init__(self, token, lex,filename):
        self.filename = filename
        self.token = token
        self.lex = lex


    def erro(self):
        Tools.print_f("          ERRO", self.filename)
        Tools.print_f(self.token.printToken(self.filename))
        exit()

    def printToken(self):
        if self.token.printToken(self.filename) is not None:
            self.token.printToken(self.filename)

    def programa(self):
        Tools.print_f("          Programa = Funcao Begin", self.filename)
        self.funcao()
        self.begin()
        print("          \nIt´s work!!!")
        # verificar se esta lendo um self.token ou se eh None

    def funcao(self):

        if (self.token.category == Category.FUNCTION):
            Tools.print_f("          Funcao = 'function' Tipo NomeVar 'abrPar' Lparam 'fecPar' Escopo'", self.filename)

            self.printToken()
            self.token = self.lex.nextToken()


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
            self.funcao()

        else:
            Tools.print_f("          Funcao = épsilon", self.filename)

    def begin(self):
        Tools.print_f("          Begin = 'void' 'begin' 'abrpar' 'fecpar' Escopo", self.filename)

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
        Tools.print_f("          NomeVar = 'id' VectorF", self.filename)
        if self.token.category == Category.ID:
            self.printToken()
            self.token = self.lex.nextToken()
            self.vector_f()
        else:
            self.erro()

    def vector(self):
        if self.token.category == Category.VECTOR:
            Tools.print_f("          Vector = 'vector' Vectorf", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            self.vector_f()
        else:
            Tools.print_f("          Vector = épsilon", self.filename)
            return 1

    def vector_f(self):
        if self.token.category == Category.ABR_COC:
            Tools.print_f("          VectorF = 'abrCoc' e 'fecCoc'", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            self.e()

            if self.token.category == Category.FEC_COC:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()



        else:
            Tools.print_f("          VectorF = épsilon", self.filename)
            return 1



    def l_param(self):

        Tools.print_f("          Lparam = Vector Tipo NomeVar LparamF", self.filename)

        self.vector()
        self.tipo()
        self.nomeVar()
        self.l_paramf()

    def l_paramf(self):
        Tools.print_f("          LparamF = 'sepVirg' Lparam", self.filename)
        if self.token.category == Category.SEP_VIRG:
            self.printToken()
            self.token = self.lex.nextToken()
            self.l_param()

        else:
            Tools.print_f("          LparamF = épsilon", self.filename)


    def tipo(self):

        if self.token.category == Category.INT:
            Tools.print_f("          Tipo = 'int'", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.FLOAT:
            Tools.print_f("          Tipo = 'Float'", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.BOOL:
            Tools.print_f("          Tipo = 'BOOL", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.CHAR:
            Tools.print_f("          Tipo = 'char", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.CCHAR:
            Tools.print_f("          Tipo = 'cchar'", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.VOID:
            Tools.print_f("          Tipo = 'void", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()

        else:
            return 1
        
    def escopo(self):
        Tools.print_f("          Escopo = 'abrCh' Comandos 'FecCh", self.filename)
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
            Tools.print_f("          Comandos = épsilon", self.filename)

        else:
            self.comandos()


    def cmd(self):
        if self.token.category == Category.READ:
            Tools.print_f("          Comandos = Cmd Comandos", self.filename)
            Tools.print_f("          Cmd = Read", self.filename)
            self.read()

        elif self.token.category == Category.PUT:
            Tools.print_f("          Comandos = Cmd Comandos", self.filename)
            Tools.print_f("          Cmd = Put", self.filename)
            self.put()

        elif self.token.category == Category.WHILE:
            Tools.print_f("          Comandos = Cmd Comandos", self.filename)
            Tools.print_f("          Cmd = While", self.filename)
            self._while()

        elif self.token.category == Category.IF:
            Tools.print_f("          Comandos = Cmd Comandos", self.filename)
            Tools.print_f("          Cmd = IF", self.filename)
            self._if()

        elif self.token.category == Category.FOR:
            Tools.print_f("          Comandos = Cmd Comandos", self.filename)
            Tools.print_f("          Cmd = For", self.filename)
            self._for()

        elif self.token.category == Category.ID:
            Tools.print_f("          Comandos = Cmd Comandos", self.filename)
            Tools.print_f("          Cmd = 'id' CmdF 'sepPtv'", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            self.cmd_f()

            if self.token.category == Category.SEP_P_VIRG:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()


        elif self.token.category == Category.VECTOR:
            Tools.print_f("          Comandos = Cmd Comandos", self.filename)
            Tools.print_f("          Cmd = VectorDecl Tipo Decl", self.filename)
            self.vectorDecl()
            if self.token.category == Category.SEP_P_VIRG:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

        elif self.tipo() != 1:
            Tools.print_f("          Cmd = Tipo Decl 'SepPtv", self.filename)
            self.decl()

            if self.token.category == Category.SEP_P_VIRG:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

        elif self.token.category == Category.BREAK:
            Tools.print_f("          Comandos = Cmd Comandos", self.filename)
            Tools.print_f("          Cmd = 'break' 'sepptv'", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()

            if self.token.category == Category.SEP_P_VIRG:
                self.printToken()
                self.token = self.lex.nextToken()

            else:
                self.erro()

        elif self.token.category == Category.RETURN:
            Tools.print_f("          Comandos = Cmd Comandos", self.filename)
            Tools.print_f("          Cmd = 'return' e 'sepPtv", self.filename)
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
            Tools.print_f("          VectorDecl = 'vector' Tipo Decl", self.filename)
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
        Tools.print_f("          Tipo = NomeVar AtbDecl", self.filename)
        self.nomeVar()
        self.declR()
        self.atb_decl()

    def declR(self):
        if self.token.category == Category.SEP_VIRG:
            Tools.print_f("          DeclR = 'sepVirg' Decl", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            self.decl()
        else:
            Tools.print_f("          DeclR = 'épsilon", self.filename)


    def chamada_func(self):
        Tools.print_f("          ChamadaFuncao = 'abrPar' Lchamada 'fecPar'", self.filename)
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
        Tools.print_f("          Lchamada = e lchamdaf", self.filename)
        self.e()
        self.l_chamadaf()

    def l_chamadaf(self):

        if self.token.category == Category.SEP_VIRG:
            Tools.print_f("          LchamadaF = 'sepVir' e Lchamda f", self.filename)
            self.token = self.lex.nextToken()
            self.e()
            self.l_chamadaf()
        else:
            Tools.print_f("          LchamadaF = épsilon", self.filename)

    def atb_decl(self):

        if self.token.category == Category.ATRIBUICAO:
            Tools.print_f("          AtbDecl = 'atribuicao' e", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            self.e()

        else:
            Tools.print_f("          AtbDecl = épsilon", self.filename)

    def read(self):
        Tools.print_f("          Read = 'read' 'abrPar' 'simpleAsp' 'cadCaracter' 'simpleAsp' 'sepVir' NomeVar 'fecPar' 'SepPVirg'", self.filename)
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

            if self.token.category == Category.SEP_VIRG:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

            self.nomeVar()

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
        Tools.print_f("          Put = 'put' 'abrPar' 'simpleAsp' 'cadCaracter' 'simpleAsp' 'sepVir' Putr 'fecPar' 'sepPVirg", self.filename)
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

            if self.token.category == Category.SEP_VIRG:
                self.printToken()
                self.token = self.lex.nextToken()
            else:
                self.erro()

            self.putR()

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






    def putR(self):
        if self.token.category == Category.SIMPLE_ASP:
            Tools.print_f("          Putr = 'simpleAsp' 'cadCaracter' 'simpleAsp'", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()

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

        else:
            Tools.print_f("          Putr = E", self.filename)
            self.e()





    def cmd_f(self):
        if self.token.category == Category.ABR_PAR:
            Tools.print_f("          CmdF = ChamadaFuncao", self.filename)
            self.chamada_func()

        elif self.token.category == Category.ABR_COC:
            Tools.print_f("          CmdF = 'abrCoc' e 'fecCoc' Atribuicao", self.filename)
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
            Tools.print_f("          CmdF = Atribuicao", self.filename)
            self.atribuicao()



    def atribuicao(self):
        if self.token.category == Category.ATRIBUICAO:
            Tools.print_f("          Atribuicao = 'atribuicao' e", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            self.e()
        else:
            self.erro()




    def _while(self):
        Tools.print_f("          While = 'while' 'abrPar' E 'fecPar' Escopo", self.filename)
        if self.token.category == Category.WHILE:
            self.printToken()
            self.token = self.lex.nextToken()
        else:
            Tools.print_f("          while esperado", self.filename)

        if self.token.category == Category.ABR_PAR:
            self.printToken()
            self.token = self.lex.nextToken()
        else:
            Tools.print_f("          ABRPAR esperado", self.filename)

        self.e()

        if self.token.category == Category.FEC_PAR:
            self.printToken()
            self.token = self.lex.nextToken()
        else:
            Tools.print_f("          FECPAR esperado", self.filename)

        self.escopo()

    def _if(self):
        Tools.print_f("          If = 'if' 'abrPar' E 'fecPar' Escopo Else", self.filename)
        if self.token.category == Category.IF:
            self.printToken()
            self.token = self.lex.nextToken()
        else:
            Tools.print_f("          if esperado", self.filename)

        if self.token.category == Category.ABR_PAR:
            self.printToken()
            self.token = self.lex.nextToken()
        else:
            Tools.print_f("          ABRPAR esperado", self.filename)

        self.e()

        if self.token.category == Category.FEC_PAR:
            self.printToken()
            self.token = self.lex.nextToken()
        else:
            Tools.print_f("          FECPAR esperado", self.filename)

        self.escopo()
        self._else()

    def _else(self):

        if self.token.category == Category.ELSE:
            Tools.print_f("          Else = 'else' Escopo", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            self.escopo()

        else:
            Tools.print_f("          Else = épsilon", self.filename)


    def _for(self):
        Tools.print_f("          For = 'for' 'abrPar' NomeVar 'in' E 'to' E 'do' Escopo", self.filename)
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
        Tools.print_f("          E = Eb Ebr", self.filename)
        self.eb()
        self.ebr()

    def eb(self):
        Tools.print_f("          Eb = Tb Ebr", self.filename)
        self.tb()
        self.ebr()

    def ebr(self):
        if self.token.category == Category.OP_OR:
            Tools.print_f("          Ebr = 'opOr' Tb Tbr", self.filename)
            self.tb()
            self.tbr()

        else:
            Tools.print_f("          Ebr = épsilon", self.filename)


    def tb(self):
        Tools.print_f("          Tb = Fb Tbr", self.filename)
        self.fb()
        self.tbr()

    def tbr(self):
        if self.token.category == Category.OP_AND:
            Tools.print_f("          Tbr = 'opAnd' Fb Tbr", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            self.fb()
            self.tbr()

        else:
            Tools.print_f("          Tbr = épsilon", self.filename)

    def fb(self):
        if self.token.category == Category.OP_NOT:
            Tools.print_f("          Fb = opNot RelUm", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            self.relUm()

        else:
            Tools.print_f("          Fb = RelUm", self.filename)
            self.relUm()

    def relUm(self):
        Tools.print_f("          RelUm = RelDois RelUmF", self.filename)
        self.relDois()
        self.relUmf()

    def relUmf(self):
        if self.token.category == Category.OP_MA:
            Tools.print_f("          RelUmF = 'opMa' RelDois", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            self.relDois()

        elif self.token.category == Category.OP_ME:
            Tools.print_f("          RelUmF = 'opMe' RelDois", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            self.relDois()

        elif self.token.category == Category.OP_MAIGU:
            Tools.print_f("          RelUmF = 'opMaigu' RelDois", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            self.relDois()

        elif self.token.category == Category.OP_MEIGU:
            Tools.print_f("          RelUmF = 'opMeigu' RelDois", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            self.relDois()

        else:
            Tools.print_f("          RelUmf = épsilon", self.filename)

    def relDois(self):
        Tools.print_f("          RelDois = Concat RelDoisF", self.filename)
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
        Tools.print_f("          Concat = Ea ConcatR", self.filename)
        self.ea()
        self.concatr()

    def concatr(self):
        if self.token.category == Category.OP_CONC:
            Tools.print_f("          ConcatR = 'opconc' Ea ConcatR", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            self.ea()
            self.concatr()
        else:
            Tools.print_f("          ConcatR = épsilon", self.filename)

    def ea(self):
        Tools.print_f("          Ea = Ta Ear", self.filename)
        self.ta()
        self.ear()

    def ear(self):
        if self.opa() == 1:
            Tools.print_f("          Ear = épsilon", self.filename)
        else:
            Tools.print_f("          Ear = ta Ear", self.filename)
            self.ta()
            self.ear()

    def opa(self):
        if self.token.category == Category.OP_ADD:
            Tools.print_f("          Opa = 'opAdd'", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.OP_SUB:
            Tools.print_f("          Opa = 'opSub'", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()

        else :
            return 1

    def ta(self):
        Tools.print_f("          Ta = Unario Tar", self.filename)
        self.unario()
        self.tar()

    def tar(self):
        if self.opm() == 0:
            Tools.print_f("          Tar = Opm Unario Tar", self.filename)
            self.unario()
            self.tar()
        else:
            Tools.print_f("          Tar = épsilon", self.filename)

    def unario(self):
        if self.token.category == Category.OP_UNA:
            Tools.print_f("          Unario = 'opUna' Fa", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            self.fa()

        else:
            Tools.print_f("          Unario = Fa", self.filename)
            self.fa()

    def opm(self):
        if self.token.category == Category.OP_MULT:
            Tools.print_f("          Opm = 'opMult'", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            return 0

        elif self.token.category == Category.OP_DIV:
            Tools.print_f("          Opm = 'opDiv'", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            return 0

        elif self.token.category == Category.OP_RET:
            Tools.print_f("          Opm = 'opRet", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            return 0

        else:
            return 1

    def fa(self):
        if self.token.category == Category.CONST_INT:
            Tools.print_f("          Fa = 'constInt'", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.CONST_FLO:
            Tools.print_f("          Fa = 'constFlo'", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.CONST_CHA:
            Tools.print_f("          Fa = 'ConstCha'", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.CONST_CCHAR:
            Tools.print_f("          Fa = 'constCchar'", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.TRUE:
            Tools.print_f("          Fa = 'True'", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.FALSE:
            Tools.print_f("          Fa = 'False'", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()

        elif self.token.category == Category.ID:
            Tools.print_f("          Fa = 'Id' Far", self.filename)
            self.printToken()
            self.token = self.lex.nextToken()
            self.far()

    def far(self):
        if self.token.category == Category.ABR_PAR:
            Tools.print_f("          Far = 'abrPar' ChamadaFuncao", self.filename)
            self.chamada_func()

        else:
            Tools.print_f("          Far = VectorF", self.filename)
            self.vector_f()



















