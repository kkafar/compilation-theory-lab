

class Node(object):
    count = 0

    def __init__ ( self , children=None ) :
        print(children)

        self.ID = str ( Node.count )
        Node.count += 1

        if not children : self.children = [ ]
        
        elif hasattr ( children , '__len__ ' ) :
            self.children = children
        else:
            self.children = [ children ]
            self.next = [ ]


class IntNum(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

class FloatNum(Node):

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

        self.children += [left, right]

class RelopExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

        self.children += [left, right]

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

class Empty(Node):
    pass



# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass
      
