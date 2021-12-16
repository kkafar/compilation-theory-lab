#!/usr/bin/python

import AST
from SymbolTable import SymbolTable, ScopeName, VariableSymbol

# I assume python3.10 notation is not available on lab PC
from typing import Union, Tuple, Literal

# Custom types
# Literals might be of use here or maybe Enums
Integer_t = 'Integer'
Float_t = 'Float'
String_t = 'String'
VariableName_t = String_t
Matrix_t = 'Matrix'
Vector_t = 'Vector'
Bool_t = 'Bool'
Variable_t = Union[
    Integer_t,
    Float_t,
    String_t,
    Matrix_t,
    Vector_t,
    Bool_t
]
VisitReturn_t = Union[
    Variable_t,
    VariableName_t
]

numeric_types = {Integer_t, Float_t}
function_names = {'zeros', 'ones', 'eye'}

std_operation_type_table = {
    Integer_t: {
        Float_t: Float_t,
        Integer_t: Integer_t
    },
    Float_t: {
        Float_t: Float_t,
        Integer_t: Float_t
    }
}

arithmetic_ops = {'+', '-', '*', '/'}
arithmetic_self_assign_ops = {'+=', '-=', '*=', '/='}
arithmetic_matrix_ops = {'.+', '.-', '.*', './'}
assign_op = '='

type_table = {
    op: std_operation_type_table for op in arithmetic_ops
}


def log_type_error(line, error_message):
    print(f"At line: {line} | {error_message}.")


def log_type_checker_error(line, error_message):
    log_type_error(line, "TypeChecker error: " + error_message)



class NodeVisitor(object):

    def visit(self, node: AST.Node) -> VisitReturn_t:
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    # Called if no explicit visitor function exists for a node.
    def generic_visit(self, node):
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)

    # simpler version of generic_visit, not so general
    # def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)


class TypeChecker(NodeVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()

    def visit_Program(self, node: AST.Program):
        self.visit(node.instructions)

    def visit_Instructions(self, node: AST.Instructions):
        for instruction in node.instructions:
            self.visit(instruction)

    def visit_IntNum(self, node: AST.IntNum) -> Integer_t:
        return Integer_t

    def visit_FloatNum(self, node: AST.FloatNum) -> Float_t:
        return Float_t

    def visit_StringValue(self, node: AST.StringValue) -> String_t:
        return String_t

    def visit_Variable(self, node: AST.Variable) -> Tuple[VariableName_t, Variable_t]:
        var_t = self.symbol_table.get(node.name)
        if var_t is not None:
            return var_t.type
        else:
            log_type_error(node.lineno, f'Undefined variable: {node.name}')

    def visit_BinExpr(self, node: AST.BinExpr) -> numeric_types:
        type1 = self.visit(node.left)
        type2 = self.visit(node.right)
        op = node.op

        if isinstance(type1, Tuple):
            type1, dims1 = type1

        if isinstance(type2, Tuple):
            type2, dims2 = type2

        if type1 is not None and type2 is not None:
            if op in arithmetic_ops:
                if type1 == Matrix_t or type2 == Matrix_t:
                    if type1 != type2 or op == '/':
                        log_type_error(node.lineno, f'{type1} {type2} not compatible with {op}')
                    elif op in {'+', '-'}:
                        if dims1 != dims2:
                            log_type_error(node.lineno,
                                           f'Cannot use {op} with matrices of different shapes ({dims1} and {dims2})')
                        else:
                            return Matrix_t, dims1
                    elif op == '*':
                        if dims1[1] != dims2[0]:
                            log_type_error(node.lineno,
                                           f'Cannot use {op} with matrices of incompatible shapes ({dims1} and {dims2})')
                        else:
                            return Matrix_t, (dims1[0], dims2[1])

                if type1 == Vector_t or type2 == Vector_t:
                    if type1 != type2 or op == '/':
                        log_type_error(node.lineno, f'{type1} {type2} not compatible with {op}')
                    elif dims1 != dims2:
                        log_type_error(node.lineno,
                                       f'Cannot use {op} with vectors of different lengths ({dims1} and {dims2})')
                    else:
                        return Vector_t, dims1

                elif type1 not in numeric_types or type2 not in numeric_types:
                    log_type_error(node.lineno, f'{type1} {type2} not compatible with {op}')
                else:
                    return type_table[op][type1][type2]

            elif op in arithmetic_matrix_ops:
                if type1 != Matrix_t or type2 != Matrix_t:
                    log_type_error(node.lineno, f'{type1} {type2} not compatible with {op}')
                elif dims1 != dims2:
                    log_type_error(node.lineno, f'Cannot use {op} with matrices of different shapes ({dims1} and {dims2})')
            else:
                log_type_checker_error("BinExpr: Unhandled arithmetic operation?!")
        else:
            log_type_error(node.lineno, "BinExpr: undefined operand")

    def visit_RelopExpr(self, node: AST.RelopExpr) -> Bool_t:
        type1 = self.visit(node.left)
        type2 = self.visit(node.right)
        op = node.op

        if type1 is not None and type2 is not None:
            if type1 == String_t or type2 == String_t:
                if type1 != type2:
                    log_type_error(node.lineno, f'{type1} {type2} not comparable')
            elif type1 not in numeric_types or type2 not in numeric_types:
                log_type_error(node.lineno, f'{type1} {type2} not comparable')

        return Bool_t

    def visit_UnaryExpr(self, node):
        operator = node.operator
        operand_t = self.visit(node.operand)

        if operator == '-':
            if operand_t in numeric_types:
                node.value = -node.operand.value
                return operand_t
            else:
                log_type_error(node.lineno, f'Invalid operand type for operator \'-\'')
        elif operator == 'TRANSPOSE':
            if isinstance(operand_t, Tuple) and operand_t[0] == Matrix_t:
                return Matrix_t, (operand_t[1][1], operand_t[1][0])
            else:
                log_type_error(node.lineno, f'Invalid operand type for operator \'\'\'')

    def visit_Assignment(self, node: AST.Assignment):
        op = node.op
        right_t = self.visit(node.right)

        if op == '=':
            if isinstance(node.left, AST.Slice):
                left_t = self.visit(node.left)
                if right_t not in numeric_types:
                    log_type_error(node.lineno, f"Cannot assign {right_t} to a {left_t[0]} cell")
            else:
                self.symbol_table.put(
                    node.left.name, VariableSymbol(node.left.name, right_t))
        elif op in arithmetic_self_assign_ops:
            left_t = self.visit(node.left)
            if isinstance(node.left, AST.Slice):
                if right_t not in numeric_types:
                    log_type_error(node.lineno, f"Cannot assign {right_t} to a {left_t[0]} cell")
            elif left_t != right_t and left_t is not None:
                log_type_error(node.lineno, f"Incompatible operands types for '{op}' operator")

    def visit_Function(self, node: AST.Function):
        function_name = node.function
        arg_types = self.visit(node.arguments)

        if len(arg_types) > 2:
            log_type_error(node.lineno, f"Wrong number of arguments, expected 1 or 2, got {len(arg_types)}")

        dims = [None, None]
        for i, arg_type in enumerate(arg_types):
            if arg_type and arg_type != Integer_t:
                log_type_error(node.lineno, f"Argument #{i} must be Integer, not {arg_type}")
            else:
                dims[i] = node.arguments.expressions[i].value

        return Matrix_t, tuple(dims)

    def visit_Conditional(self, node: AST.Conditional):
        self.symbol_table.push_scope(ScopeName.IF)
        self.visit(node.condition)
        self.visit(node.if_instruction)
        self.symbol_table.pop_scope()
        if node.else_instruction is not None:
            self.symbol_table.push_scope(ScopeName.ELSE)
            self.visit(node.else_instruction)
            self.symbol_table.pop_scope()

    def visit_Vector(self, node: AST.Vector):
        return Vector_t, len(node.values)

    def visit_Matrix(self, node: AST.Matrix):
        x_dim = len(node.vectors)
        y_dim = None

        for vector in node.vectors:
            vector_len = self.visit(vector)[1]
            if y_dim is None:
                y_dim = vector_len
            elif y_dim != vector_len:
                log_type_error(node.lineno, f"Matrix initialized with vectors of different lengths")
                return Matrix_t, (x_dim, None)

        return Matrix_t, (x_dim, y_dim)

    def visit_JumpStatement(self, node: AST.JumpStatement):
        # break or continue
        # we need to make sure, we are in (while|for) scope!

        if not self.symbol_table.is_in_loop_scope():
            log_type_error(node.lineno, f'Jump statement NOT in loop scope')

        if node.statement not in {'BREAK', 'CONTINUE'}:
            log_type_checker_error(node.lineno, f'Unhandled JumpStatement')

        return None

    def visit_PrintStatement(self, node: AST.PrintStatement):
        self.visit(node.expressions)
        return None

    def visit_Expressions(self, node: AST.Expressions):
        types = []

        for expression in node.expressions:
            types.append(self.visit(expression))

        return types

    def visit_ReturnStatement(self, node: AST.ReturnStatement):
        if node.expression is not None:
            return self.visit(node.expression)
        return None

    def visit_WhileLoop(self, node: AST.WhileLoop):
        self.symbol_table.push_scope(ScopeName.WHILE)

        expression_t = self.visit(node.expression)
        if expression_t != Bool_t and expression_t is not None:
            log_type_error(node.lineno, f'WhileLoop expression must return Bool, not {expression_t}')

        if node.instruction is not None:
            self.visit(node.instruction)

        self.symbol_table.pop_scope()
        return None

    def visit_ForLoop(self, node: AST.ForLoop):
        self.symbol_table.push_scope(ScopeName.FOR)

        # we do not check for name shadowing
        # iterator = self.visit(node.variable)

        # these two below should be of Integer type
        # & we need to check for it, because if they were passed as ID
        # scanner did not verify their type
        left = self.visit(node.range_value_left)
        right = self.visit(node.range_value_right)

        self.symbol_table.put(node.variable.name, VariableSymbol(
            node.variable.name, Integer_t))

        if left != Integer_t and left is not None:
            log_type_error(node.lineno, f"Left range boundary must be of integer type, not {left}")
        if right != Integer_t and right is not None:
            log_type_error(node.lineno, f"Right range boundary must be of integer type, not {right}")

        self.visit(node.instruction)
        self.symbol_table.pop_scope()

    def visit_Slice(self, node: AST.Slice):
        symbol = self.symbol_table.get(node.name)
        indices = self.visit(node.vector)

        if not symbol:
            log_type_error(node.lineno, f"Reference to undefined variable: {node.name}")
            return  # handle NullPointerException

        # matrix
        if not isinstance(symbol.type, Tuple):
            log_type_error(node.lineno, f"{symbol.type} is not subscriptable")
            return

        symbol_type = symbol.type[0]
        dims = symbol.type[1]

        if symbol_type == Matrix_t:
            if len(indices) != 2 and isinstance(dims, Tuple) and len(dims) == 2:
                log_type_error(node.lineno,
                               f"Provided {len(indices)} {'index' if len(indices) == 1 else 'indices'}, 2 required")
            else:
                for i in range(2):
                    if indices[i] and dims[i] and (indices[i] < 0 or indices[i] >= dims[i]):
                        log_type_error(node.lineno,
                                       f"Index {indices[i]} is out of range for matrix {symbol.name} with shape {dims} at axis {i}")

        # vector
        elif symbol_type == Vector_t:
            if len(indices) != 1:
                log_type_error(node.lineno, f"Provided {len(indices)} indices for vector {symbol.name}, 1 required")
            elif indices[0] and dims and (indices[0] < 0 or indices[0] >= dims):
                log_type_error(node.lineno, f"Index {indices[0]} is out of range for vector with length {dims}")

        else:
            log_type_error(node.lineno, f"{symbol.type} is not subscritable")

        return symbol_type, dims

    def visit_SliceVector(self, node: AST.SliceVector):
        '''
            returns list of indices in slice_vector
            if index isn't a constant Integer, then it's of NoneType in the list
        '''
        indices = [None] * len(node.values)
        for i, value in enumerate(node.values):
            value_type = self.visit(value)
            if value_type == Integer_t:
                if isinstance(value, AST.IntNum):
                    indices[i] = value.value
            else:
                log_type_error(node.lineno, f"{value_type} cannot be used as an index for a matrix or vector")

        return indices

