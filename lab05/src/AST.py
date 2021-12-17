class Node(object):
    count = 0

    def __init__(self, children=None):
        self.ID = str(Node.count)
        Node.count += 1
        self.lineno = None

        if not children:
            self.children = []

        elif hasattr(children, '__len__ '):
            self.children = children
            print(children, self.children)
        else:
            self.children = [children]
            self.next = []


class Program(Node):
    def __init__(self, instructions=None):
        super().__init__()
        self.instructions = instructions
    

class IntNum(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value


class FloatNum(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value


class StringValue(Node):
    def __init__(self, string):
        super().__init__()
        self.string = string


class Variable(Node):
    def __init__(self, name):
        super().__init__()
        self.name = name


class BinExpr(Node):
    def __init__(self, op, left, right):
        super().__init__()
        self.op = op
        self.left = left
        self.right = right

        self.children = [left, right]


class RelopExpr(Node):
    def __init__(self, op, left, right):
        super().__init__()
        self.op = op
        self.left = left
        self.right = right

        self.children = [left, right]


class UnaryExpr(Node):
    def __init__(self, operator, operand):
        super().__init__()
        self.operator = operator
        self.operand = operand


class RelExpr(Node):
    def __init__(self, op, left, right):
        super().__init__()
        self.op = op
        self.left = left
        self.right = right


class Instructions(Node):
    def __init__(self, instruction):
        super().__init__()
        if hasattr(instruction, '__len__'):
            self.instructions = instruction
        else:
            self.instructions = [instruction]


class Assignment(Node):
    def __init__(self, op, left, right):
        super().__init__()
        self.op = op
        self.left = left
        self.right = right


class Function(Node):
    def __init__(self, function, arguments):
        super().__init__()
        self.function = function
        self.arguments = arguments


class Conditional(Node):
    def __init__(self, condition, if_instruction, else_instruction=None):
        super().__init__()
        self.condition = condition
        self.if_instruction = if_instruction
        self.else_instruction = else_instruction


class Vector(Node):
    def __init__(self, value=None):
        if value is None:
            self.values = []
        else:
            self.values = [value]

class Matrix(Node):
    def __init__(self, vector=None):
        super().__init__()
        if vector is None:
            self.vectors = []
        else:
            self.vectors = [vector]

class JumpStatement(Node):
    def __init__(self, statement):
        super().__init__()
        self.statement = statement


class PrintStatement(Node):
    def __init__(self, expressions):
        super().__init__()
        self.expressions = expressions


class ReturnStatement(Node):
    def __init__(self, expression=None):
        super().__init__()
        self.expression = expression


class Expressions(Node):
    def __init__(self, expression=None):
        super().__init__()
        if expression is not None:
            self.expressions = [expression]
        else:
            self.expressions = []


class WhileLoop(Node):
    def __init__(self, expression, instruction):
        super().__init__()
        self.expression = expression
        self.instruction = instruction


class ForLoop(Node):
    def __init__(self, variable, range_value_left, range_value_right, instruction):
        super().__init__()
        self.variable = variable
        self.range_value_left = range_value_left
        self.range_value_right = range_value_right
        self.instruction = instruction


class Slice(Node):
    def __init__(self, matrix, vector):
        super().__init__()
        self.name = matrix
        self.vector = vector

class SliceVector(Node):
    def __init__(self, values):
        super().__init__()
        self.values = values


class Empty(Node):
    pass


class Error(Node):
    pass
