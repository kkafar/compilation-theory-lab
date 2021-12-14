from __future__ import print_function
import AST


def addToClass(cls):

    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


class TreePrinter:

    @addToClass(AST.Program)
    def printTree(self, indent=0):
        if self.instructions:
            self.instructions.printTree()

    @addToClass(AST.Instructions)
    def printTree(self, indent=0):
        for instruction in self.instructions:
            instruction.printTree(indent)

    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print(self.value)

    @addToClass(AST.FloatNum)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print(self.value)

    @addToClass(AST.StringValue)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print(f'"{self.string}"')

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

        self.arguments.printTree(indent+1)

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
        print(self.name)

        self.vector.printTree(indent+1)

    @addToClass(AST.PrintStatement)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print('PRINT')

        self.expressions.printTree(indent+1)

    @addToClass(AST.ReturnStatement)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print('RETURN')

        if self.expression:
            self.expression.printTree(indent+1)

    @addToClass(AST.JumpStatement)
    def printTree(self, indent=0):
        print("|  "*indent, end='')
        print(self.statement.upper())

    @addToClass(AST.Empty)
    def printTree(self, indent=0):
        pass

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
