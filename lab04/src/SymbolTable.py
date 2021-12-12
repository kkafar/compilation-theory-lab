#!/usr/bin/python

class Symbol(object):
    pass


class VariableSymbol(Symbol):
    def __init__(self, name, _type):
        self.name = name
        self.type = _type


class SymbolTable(object):
    def __init__(self, parent=None, name='global'):  # parent scope and symbol table name
        self.symbols = {}
        self.parent_scope = parent
        self.scope_name = name
        self.scope = 0

    def put(self, name, symbol):  # put variable symbol or fundef under <name> entry
        self.symbols[name] = symbol

    def get(self, name):  # get variable symbol or fundef from <name> entry
        return self.symbols[name]

    def get_parent_scope(self):
        return self.parent_scope

    def push_scope(self, name):
        self.scope += 1

    def pop_scope(self):
        if self.scope == 0:
            raise RuntimeError("Can not decrease scope!")
        self.scope -= 1
