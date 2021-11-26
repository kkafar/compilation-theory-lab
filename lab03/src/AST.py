

class Node(object):
    count = 0

    def __init__(self, children=None):
        self.ID = str(Node.count)
        Node.count += 1

        if not children:
            self.children = []

        elif hasattr(children, '__len__ '):
            self.children = children
            print(children, self.children)
        else:
            self.children = [children]
            self.next = []


class Constant(Node):
    def __init__(self, value):
        self.value = value


class Variable(Node):
    def __init__(self, name):
        self.name = name


class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

        self.children = [left, right]


class RelopExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

        self.children = [left, right]


class UnaryExpr(Node):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand


class RelExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class Instructions(Node):
    def __init__(self, children):
        super().__init__(children)


class Assignment(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class Function(Node):
    def __init__(self, function, expressions):
        self.function = function
        self.expressions = expressions


class Conditional(Node):
    def __init__(self, condition, if_instruction, else_instruction=None):
        self.condition = condition
        self.if_instruction = if_instruction
        self.else_instruction = else_instruction


class Vector(Node):
    def __init__(self, value=None):
        if value is None:
            self.values = []
        else:
            self.values = [value]


class Statement(Node):
    def __init__(self, statement, expression=None):
        self.statement = statement
        self.expression = expression


class Expressions(Node):
    def __init__(self, expression=None):
        if expression is not None:
            self.expressions = [expression]
        else:
            self.expressions = []


class WhileLoop(Node):
    def __init__(self, expression, instruction):
        self.expression = expression
        self.instruction = instruction


class ForLoop(Node):
    def __init__(self, variable, range_value_left,  range_value_right,  instruction):
        self.variable = variable
        self.range_value_left = range_value_left
        self.range_value_right = range_value_right
        self.instruction = instruction


class Slice(Node):
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.vector = vector


class Empty(Node):
    pass


class Error(Node):
    def __init__(self):
        pass
