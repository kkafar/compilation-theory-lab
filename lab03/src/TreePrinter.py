from __future__ import print_function
import AST


def addToClass(cls):

    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        for child in self.children:
            child.printTree(indent)

    @addToClass(AST.Instructions)
    def printTree(self, indent=0):
        for child in self.children:
            child.printTree(indent)

    @addToClass(AST.Constant)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print(self.value)

    @addToClass(AST.Assignment)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print(self.op)

        self.left.printTree(indent+1)
        self.right.printTree(indent+1)

    @addToClass(AST.BinExpr)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print(self.op)

        self.left.printTree(indent+1)
        self.right.printTree(indent+1)

    @addToClass(AST.RelopExpr)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print(self.op)

        self.left.printTree(indent+1)
        self.right.printTree(indent+1)

    @addToClass(AST.UnaryExpr)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print(self.operator)

        self.operand.printTree(indent+1)

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print(self.name)

    @addToClass(AST.Function)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print(self.function)

        self.expressions.printTree(indent+1)

    @addToClass(AST.Conditional)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print("IF")
        self.condition.printTree(indent+1)

        print("|  "*indent, end='')
        print("THEN")
        self.if_instruction.printTree(indent+1)

        if self.else_instruction:
            print("|  "*indent, end='')
            print("ELSE")
            self.else_instruction.printTree(indent+1)

    @addToClass(AST.Expressions)
    def printTree(self, indent=0):
        for expression in self.expressions:
            expression.printTree(indent)

    @addToClass(AST.WhileLoop)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print('WHILE')

        self.expression.printTree(indent+1)
        self.instruction.printTree(indent+1)

    @addToClass(AST.ForLoop)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print('FOR')

        self.variable.printTree(indent+1)

        print("|  "*(indent+1), end='')
        print('RANGE')
        self.range_value_left.printTree(indent+2)
        self.range_value_right.printTree(indent+2)
        self.instruction.printTree(indent+1)

    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print('VECTOR')

        for value in self.values:
            value.printTree(indent+1)

    @addToClass(AST.Slice)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print('REF')

        print("|  "*(indent+1), end='')
        print(self.matrix)

        self.vector.printTree(indent+1)

    @addToClass(AST.Statement)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print(self.statement)

        if self.expression:
            self.expression.printTree(indent+1)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass

        # fill in the body

    # define printTree for other classes
    # ...
