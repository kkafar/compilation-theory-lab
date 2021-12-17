
import AST
import SymbolTable
from Memory import *
from Exceptions import  *
from visit import *
import sys

sys.setrecursionlimit(10000)

binop_func = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
    '/': lambda x, y: x/y,
    '>': lambda x, y: x>y,
    '<': lambda x, y: x<y,
    '>=': lambda x, y: x>=y,
    '<=': lambda x, y: x<=y,
    '==': lambda x, y: x==y,
    '!=': lambda x, y: x!=y,
}

class Interpreter(object):


    @on('node')
    def visit(self, node):
        pass

    @when(AST.Program)
    def visit(self, node):
        node.instructions.accept(self)

    @when(AST.Instructions)
    def visit(self, node):
        for instruction in node.instructions:
            instruction.accept(self)
        
    @when(AST.BinExpr)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)

        return binop_func[node.op](r1, r2)

    @when(AST.RelopExpr)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)

        return binop_func[node.op](r1, r2)

    @when(AST.PrintStatement)
    def visit(self, node):
        for expression in node.expressions:
            print(expression.accept())



    @when(AST.Assignment)
    def visit(self, node):
        pass
    #
    #

    # simplistic while loop interpretation
    @when(AST.WhileLoop)
    def visit(self, node):
        r = None
        while node.cond.accept(self):
            r = node.body.accept(self)
        return r


