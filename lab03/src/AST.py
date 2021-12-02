

class Constant:
    def __init__(self, value):
        self.value = value


class IntNum:
    def __init__(self, value):
        self.value = value


class FloatNum:
    def __init__(self, value):
        self.value = value


class StringValue:
    def __init__(self, string):
        self.string = string


class Variable:
    def __init__(self, name):
        self.name = name


class BinExpr:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

        self.children = [left, right]


class RelopExpr:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

        self.children = [left, right]


class UnaryExpr:
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand


class RelExpr:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class Instructions:
    def __init__(self, instruction):
        if hasattr(instruction, '__len__'):
            self.instructions = instruction
        else:
            self.instructions = [instruction]


class Assignment:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class Function:
    def __init__(self, function, expressions):
        self.function = function
        self.expressions = expressions


class Conditional:
    def __init__(self, condition, if_instruction, else_instruction=None):
        self.condition = condition
        self.if_instruction = if_instruction
        self.else_instruction = else_instruction


class Vector:
    def __init__(self, value=None):
        if value is None:
            self.values = []
        else:
            self.values = [value]


class Statement:
    def __init__(self, statement, expression=None):
        self.statement = statement
        self.expression = expression


class Expressions:
    def __init__(self, expression=None):
        if expression is not None:
            self.expressions = [expression]
        else:
            self.expressions = []


class WhileLoop:
    def __init__(self, expression, instruction):
        self.expression = expression
        self.instruction = instruction


class ForLoop:
    def __init__(self, variable, range_value_left,  range_value_right,  instruction):
        self.variable = variable
        self.range_value_left = range_value_left
        self.range_value_right = range_value_right
        self.instruction = instruction


class Slice:
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.vector = vector


class Empty:
    pass


class Error:
    def __init__(self):
        pass
