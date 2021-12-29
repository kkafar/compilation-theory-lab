
import AST
import SymbolTable
from Memory import *
from Exceptions import *
from visit import *
import sys
import numpy as np

sys.setrecursionlimit(10000)

binop_func = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
    '/': lambda x, y: x/y,
    '>': lambda x, y: x > y,
    '<': lambda x, y: x < y,
    '>=': lambda x, y: x >= y,
    '<=': lambda x, y: x <= y,
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y,
}

unary_func = {
    '-': lambda x: -x,
    'TRANSPOSE': lambda x: x.T
}

matrix_func = {
    'zeros': lambda x: np.zeros(x) if not isinstance(x, tuple) else np.zeros(*x),
    'ones': lambda x: np.ones(x) if not isinstance(x, tuple) else np.ones(*x),
    'eye': lambda x: np.eye(x) if not isinstance(x, tuple) else np.eye(*x)
}

memory_stack = MemoryStack()


class Interpreter(object):

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Program)
    def visit(self, node):
        node.instructions.accept(self)

    @when(AST.IntNum)
    def visit(self, node):
        return node.value

    @when(AST.FloatNum)
    def visit(self, node):
        return node.value

    @when(AST.StringValue)
    def visit(self, node):
        return node.string

    @when(AST.Variable)
    def visit(self, node):
        return memory_stack.get(node.name)

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

    @when(AST.UnaryExpr)
    def visit(self, node):
        operator = node.operator.accept(self)
        return unary_func[node.operand](operator)

    @when(AST.Instructions)
    def visit(self, node):
        for instruction in node.instructions:
            instruction.accept(self)

    @when(AST.Assignment)
    def visit(self, node):
        if node.op == '=':
            value = node.right.accept(self)
            memory_stack.set(node.left.name, value)
        else:
            raise Exception('unimplemented')

    @when(AST.Function)
    def visit(self, node):
        arguments = node.arguments.accept(self)
        return matrix_func[node.function](arguments)

    @when(AST.Conditional)
    def visit(self, node):
        if node.condition.accept(self):
            node.if_instruction.accept(self)
        elif node.else_instruction is not None:
            node.else_instruction.accept(self)

    @when(AST.Vector)
    def visit(self, node):
        return np.array([value.accept(self) for value in node.values])

    @when(AST.Matrix)
    def visit(self, node):
        return np.array([vector.accept(self) for vector in node.vectors])

    @when(AST.JumpStatement)
    def visit(self, node):
        if node.statement == 'break':
            raise BreakException
        elif node.statement == 'continue':
            raise ContinueException

    @when(AST.PrintStatement)
    def visit(self, node):
        expression_evals = node.expressions.accept(self)
        print(*expression_evals)

    @when(AST.ReturnStatement)
    def visit(self, node):
        sys.exit()  # ?

    @when(AST.Expressions)
    def visit(self, node):
        evals = []
        for expression in node.expressions:
            evals.append(expression.accept(self))
        return evals

    # simplistic while loop interpretation
    @when(AST.WhileLoop)
    def visit(self, node):
        while node.expression.accept(self):
            try:
                node.instruction.accept(self)
            except BreakException:
                break
            except ContinueException:
                continue

    @when(AST.ForLoop)
    def visit(self, node):

        start_value = node.range_value_left.accept(self)
        end_value = node.range_value_right.accept(self)
        memory_stack.set(node.variable.name, start_value)

        i = start_value
        while i <= end_value:
            try:
                r = node.instruction.accept(self)
            except BreakException:
                break
            except ContinueException:
                pass

            i = node.variable.accept(self) + 1
            memory_stack.set_(node.variable.name, i)

    @when(AST.Slice)
    def visit(self, node):
        indices = node.vector.accept(self)
        matrix = memory_stack.get(node.name)

        if len(indices) == 1:
            return matrix[indices[0]]
        else:
            return matrix[indices[0], indices[1]]

    @when(AST.SliceVector)
    def visit(self, node):
        values = []
        for value in node.values:
            values.append(value.accept(self))
