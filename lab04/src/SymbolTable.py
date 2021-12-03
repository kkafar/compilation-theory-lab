#!/usr/bin/python


class VariableSymbol(Symbol):

    def __init__(self, name, type):
        pass
    #


class SymbolTable:

    def __init__(self, parent=None, name='global'): # parent scope and symbol table name
        pass
    #

    def put(self, name, symbol): # put variable symbol or fundef under <name> entry
        pass
    #

    def get(self, name): # get variable symbol or fundef from <name> entry
        pass
    #

    def getParentScope(self):
        pass
    #

    def pushScope(self, name):
        pass
    #

    def popScope(self):
        pass
    #


