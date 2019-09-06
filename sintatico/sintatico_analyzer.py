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
        if self.token is not None:
            self.funcao()
            self.begin()
        else:
            print("SEM ERROS DE SINTAXE :)")
        
        # verificar se esta lendo um self.token ou se eh None

    def funcao(self):

        if (self.token.category == Category.FUNCTION):
            # print("FUNCAO")
            self.token = self.lex.nextToken()
            self.tipo()

            if self.token.category == Category.ID:
                # print("ID")

                self.token = self.lex.nextToken()

                if self.token.category == Category.ABR_PAR:
                    # print("ABRE PARENTES")
                    self.token = self.lex.nextToken()
                    self.l_param()
                    # print("CHAMOU L_PARAM")
                else:
                    print("ERRO: ABRPAR ESPERADO")
                    self.erro()
                if self.token.category == Category.FEC_PAR:
                    # print("FECHA PARAM")
                    self.token = self.lex.nextToken()
                    self.escopo()
                else:
                    print("ERRO: FEC_PAR ESPERADO")
                    self.erro()
            else:
                print("ERRO: ID ESPERADO")
                self.erro()
        else:
            pass
            # print("FUNCAO VAZIO")
            # self.erro()

    def begin(self):
        print("=== BEGIN ===")
        if self.token.category == Category.VOID:
            self.token = self.lex.nextToken()
            # print("BEGIN VOID")
            if self.token.category == Category.BEGIN:
                # print("BEGIN")
                self.token = self.lex.nextToken()

                if self.token.category == Category.ABR_PAR:
                    # print("ABR_PAR")
                    self.token = self.lex.nextToken()
                    if self.token.category == Category.FEC_PAR:
                        self.token = self.lex.nextToken()
                        # print("FEC_PAR")
                        self.escopo()
                    else:
                        # print("LPARAM")
                        self.l_param()
                        if self.token.category == Category.FEC_PAR:
                            self.token = self.lex.nextToken()
                            self.escopo()
                        else:
                            print("ERRO: FECPAR ESPERADO")
                            self.erro()
                else:
                    print("ERRO: ABR_PAR ESPERADO")
                    self.erro()

            
            else:
                print("ERRO: BEGIN ESPERADO")
                self.erro()
        else:
            print("ERRO: VOID ESPERADO")
            self.erro()

    def l_param(self):
        self.tipo()
        if self.token.category == Category.ID:
            self.token = self.lex.nextToken()
            self.l_paramf()
        else:
            print("ERRO: ID ESPERADO")
            self.erro()

    def l_paramf(self):
        # print(self.token.category)
        if self.token.category == Category.SEP_VIRG:
            self.token = self.lex.nextToken()
            self.tipo()
            if self.token.category == Category.ID:
                self.token = self.lex.nextToken()
                self.l_paramf()
        else:
            if self.token.category == Category.FEC_PAR:
                # print("FECHA CHAVE")
                pass
            else:
                print("ERRO: SEP_VIRG ESPERADO")
                self.erro()

        
    def tipo(self):
        print("=== TIPO ===")
        # print(self.token.printToken())
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

        elif self.token.category == Category.VECTOR:
            self.token = self.lex.nextToken()
        else:
            return False
            # print("ERROR: ESPERADO UM TIPO [int,float,cchar,char,bool,void]")
            # self.erro()
        
    def escopo(self):
        print("=== ESCOPO ===")
        if self.token.category == Category.ABR_CH:
            self.token = self.lex.nextToken()
            # print("TESTANDO COMANDOS")
            self.comandos()
            
        else:
            print("ERRO: ABR_CH ESPERADO")
            self.erro()

        if self.token.category == Category.FEC_CH:
            self.token = self.lex.nextToken()
            self.programa()
        else:
            print("ERRO: FEC_CH ESPERADO")
            self.erro()

    def comandos(self):
        print("=== COMANDOS ===")
        self.cmd()
        # self.comandos()

    def cmd(self):
        print("=== CMD ===")
        self.decl()
        self._put()
        self._while()
        

    def cmd_f(self):
        print("=== CMD_F ===")

    def decl(self):
        print("=== DECL ===")
        if self.tipo() is None:
            self.tipo()
            self.nome_var()
            self.atb_decl()
            self.decl_f()
        else: 
            pass

    def decl_f(self):
        print("=== DECL_F ===")
        if self.token.category == Category.SEP_P_VIRG:
            self.token = self.lex.nextToken()
        else:
            print("ERRO: SEP_VIRG ESPERADO")
            self.erro()

        # print(self.tipo())
        if self.tipo() is None:
            self.tipo()
            self.nome_var()
            self.atb_decl()
            self.decl_f()
        else: 
            pass

    def atb_decl(self):
        print("=== ATB_DECL ===")
        if self.token.category == Category.ATRIBUICAO:
            self.token = self.lex.nextToken()
            self.atb_const()
        elif self.token.category is not Category.SEP_P_VIRG:
            print("ERRO: ATRIBUICAO ESPERADO")
            self.erro()


    def atb_const(self):
        print("=== ATB_CONST ===")
        if self.token.category == Category.CAD_CARACTER:
            self.token = self.lex.nextToken()
        elif self.token.category == Category.CONST_INT:
            self.token = self.lex.nextToken()
        elif self.token.category == Category.CONST_FLO:
            self.token = self.lex.nextToken()
        elif self.token.category == Category.CONST_CHA:
            self.token = self.lex.nextToken()
        elif self.token.category == Category.CONST_CCHAR:
            self.token = self.lex.nextToken()
        elif self.token.category == Category.CONST_BOOL:
            self.token = self.lex.nextToken()
        else:
            print("ERRO: CONSTANTE ESPERADO")
            self.erro()

    def nome_var(self):
        print("=== NOME_VAR ===")
        if self.token.category == Category.ID:
            self.token = self.lex.nextToken()
        else:
            print("ERRO: ID ESPERADO")
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
                self.erro()




        



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

    

    

    def _read(self):
        print("Não implementado ainda")

    def _put(self):
        print("=== PUT ===")
        if self.token.category == Category.PUT:
            self.token = self.lex.nextToken()

            if self.token.category == Category.ABR_PAR:
                self.token = self.lex.nextToken()

                if self.token.category == Category.SIMPLE_ASP:
                    self.token = self.lex.nextToken()

                    if self.token.category == Category.CAD_CARACTER:
                        self.token = self.lex.nextToken()

                        if self.token.category == Category.SIMPLE_ASP:
                            self.token = self.lex.nextToken()

                            if self.token.category == Category.FEC_PAR:
                                self.token = self.lex.nextToken()

                                if self.token.category == Category.SEP_P_VIRG:
                                    self.token = self.lex.nextToken()
                                    pass
                                else:
                                    print("ERRO: SEP_P_VIRG ESPERADO")
                                    self.erro()
                            else:
                                print("ERRO: FEC_PAR ESPERADO")
                                self.erro()
                        else:
                            print("ERRO: SIMPLE_ASP ESPERADO")
                            self.erro()
                    else:
                        print("ERRO: CAD_CARACTER ESPERADO")
                        self.erro()
                else:
                    print("ERRO: SIMPLE_ASP ESPERADO")
                    self.erro()


    def atribuicao(self):
        if self.token.category == Category.ATRIBUICAO:
            self.token = self.lex.nextToken()
        else:
            print("Atribuicao esperado")
        self.e()


    def _while(self):
        if self.token.category == Category.WHILE:
            self.token = self.lex.nextToken()
            if self.token.category == Category.ABR_PAR:
                self.token = self.lex.nextToken()
                # self.eb()
            else:
                print("ERRO: ABR_PAR ESPERADO")
                self.erro()
            if self.token.category == Category.FEC_PAR:
                self.token = self.lex.nextToken()
            else:
                print("ERRO: FECPAR ESPERADO")
                self.erro()
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
        self.tar()

    def eunario(self):
        if self.token.category == Category.OP_NOT:
            self.token = self.lex.nextToken
            self.fa()

        else:
            self.fa()

    def fa(self):
        if self.token.category == Category.ABR_PAR:
            self.token = self.lex.nextToken
            self.e()
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
            self.erro()


