#!/usr/bin/python

from enum import Enum
from collections import defaultdict


class ScopeName(Enum):
    GLOBAL = 0,
    IF = 1,
    ELSE = 2,
    WHILE = 3,
    FOR = 4


class Symbol(object):
    pass


class VariableSymbol(Symbol):
    def __init__(self, name, _type):
        self.name = name
        self.type = _type


class SymbolTable(object):
    def __init__(self,
                 parent: 'SymbolTable' = None,
                 scope_name: ScopeName = ScopeName.GLOBAL):  # parent scope and symbol table name
        self.__symbol = defaultdict(lambda: None)
        self.parent_scope = parent
        self.__scope_name_stack = [scope_name]
        self.__scope_level = 0

    def put(self, name, symbol):  # put variable symbol or fundef under <name> entry
        self.__symbol[name] = symbol

    def get(self, name):  # get variable symbol or fundef from <name> entry
        return self.__symbol[name]

    # def get_parent_scope(self):
    #     return self.parent_scope

    def get_tightest_scope_name(self):
        return self.__scope_name_stack[-1]

    def is_in_loop_scope(self):
        return ScopeName.WHILE in self.__scope_name_stack or ScopeName.FOR in self.__scope_name_stack

    def push_scope(self, name: ScopeName):
        # print('push_scope', name.name)
        self.__scope_level += 1
        self.__scope_name_stack.append(name)

    def pop_scope(self):
        # print('pop_scope', self.get_tightest_scope_name().name)
        if self.__scope_level == 0:
            raise RuntimeError("Can not decrease scope!")
        self.__scope_name_stack.pop()
        self.__scope_level -= 1
