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
        # print('Program')
        self.visit(node.instructions)

    def visit_Instructions(self, node: AST.Instructions):
        # print('Instructions')
        for instruction in node.instructions:
            self.visit(instruction)

    def visit_IntNum(self, node: AST.IntNum) -> Integer_t:
        # print('IntNum')
        return Integer_t

    def visit_FloatNum(self, node: AST.FloatNum) -> Float_t:
        # print('FloatNum')
        return Float_t

    def visit_StringValue(self, node: AST.StringValue) -> String_t:
        # print('StringValue')
        return String_t

    def visit_Variable(self, node: AST.Variable) -> Tuple[VariableName_t, Variable_t]:
        # print('Variable')
        var_t = self.symbol_table.get(node.name)
        if var_t is not None:
            return var_t.type
        else:
            print('At line:', node.lineno, '|',
                  f'Undefined variable: {node.name}')

    def visit_BinExpr(self, node: AST.BinExpr) -> numeric_types:
        # print('BinExpr')
        type1 = self.visit(node.left)
        type2 = self.visit(node.right)
        op = node.op

        if type1 is not None and type2 is not None:
            if op in arithmetic_ops:
                if type1 not in numeric_types or type2 not in numeric_types:
                    print('At line:', node.lineno, '|',
                          f'{type1} {type2} not compatible with {op}')
                else:
                    return type_table[op][type1][type2]

            elif op in arithmetic_matrix_ops:
                if type1 != Vector_t or type2 != Vector_t:
                    print('At line:', node.lineno, '|',
                          f'{type1} {type2} not compatible with {op}')
                else:
                    return type_table[op][type1][type2]
            else:
                # this should not happen
                print("TypeChecker error: BinExpr")

    def visit_RelopExpr(self, node: AST.RelopExpr) -> Bool_t:
        # print('RelopExpr')
        type1 = self.visit(node.left)
        type2 = self.visit(node.right)
        op = node.op

        if type1 is not None and type2 is not None:
            if type1 == String_t or type2 == String_t:
                if type1 != type2:
                    print('At line:', node.lineno, '|',
                          f'{type1} {type2} not comparable')
            elif type1 not in numeric_types or type2 not in numeric_types:
                print('At line:', node.lineno, '|',
                      f'{type1} {type2} not comparable')

        # TODO (@kkafar): Should we cover matrix case?

        return Bool_t

    def visit_UnaryExpr(self, node):
        # print('UnaryExpr')
        operator = node.operator
        operand_t = self.visit(node.operand)

        if operator == '-':
            if operand_t in numeric_types:
                return operand_t
            else:
                print('At line:', node.lineno, '|',
                      'Invalid operand type for operator \'-\'.')

        if operator == 'TRANSPOSE':
            if operand_t == Vector_t:
                return operand_t
            else:
                print('At line:', node.lineno, '|',
                      'Invalid operand type for operator \'\'\'.')

    def visit_Assignment(self, node: AST.Assignment):
        # print('Assignment')
        op = node.op
        right_t = self.visit(node.right)

        if op == '=':
            self.symbol_table.put(
                node.left.name, VariableSymbol(node.left.name, right_t))
        elif op in arithmetic_self_assign_ops:
            # TODO (@kkafar): We need to check here whether type of left side == type of right side
            left_t = self.visit(node.left)
            if left_t != right_t and left_t is not None:
                print('At line:', node.lineno, '|',
                      f"Incompatible operands types for '{op}' operator.")

    def visit_Function(self, node: AST.Function):
        # print('Function')
        function_name = node.function

        arg_types = self.visit(node.arguments)

        if len(arg_types) > 2:
            print('At line:', node.lineno, '|',
                  f"Wrong number of arguments, expected 1 or 2, got {len(arg_types)}")

        for i, arg_type in enumerate(arg_types):
            if arg_type and arg_type != Integer_t:
                print('At line:', node.lineno, '|',
                      f"Argument #{i} must be Integer, not {arg_type}")

        # TODO (@kkafar): Consider using Vector_t
        # All available functions return a matrix
        return Matrix_t

    def visit_Conditional(self, node: AST.Conditional):
        # print('Conditional')
        self.symbol_table.push_scope(ScopeName.IF)
        self.visit(node.condition)
        self.visit(node.if_instruction)
        self.symbol_table.pop_scope()
        if node.else_instruction is not None:
            self.symbol_table.push_scope(ScopeName.ELSE)
            self.visit(node.else_instruction)
            self.symbol_table.pop_scope()

    def visit_Vector(self, node: AST.Vector):
        # print('Vector')
        # TODO @kkafar: Check if vector data type is checked by scanner
        return Vector_t, len(node.values)

    def visit_Matrix(self, node: AST.Matrix):
        # print('Vector')
        # TODO @kkafar: Check if vector data type is checked by scanner

        x_dim = len(node.vectors)
        y_dim = None

        for vector in node.vectors:
            vector_len = self.visit(vector)[1]
            if y_dim is None:
                y_dim = vector_len
            elif y_dim != vector_len:
                print('At line:', node.lineno, '|',
                  f"Matrix initialized with vectors of different lengths")
                break

        return Matrix_t, (x_dim, y_dim)

    def visit_JumpStatement(self, node: AST.JumpStatement):
        # print('JumpStatement')
        # break or continue
        # we need to make sure, we are in while / for scope!

        # I think we do not have to check it, scanner already does
        if not self.symbol_table.is_in_loop_scope():
            print('At line:', node.lineno, '|',
                  'Jump statement NOT in loop scope.')

        if node.statement == 'BREAK':
            # I think poping the scope in WhileLoop is enough?
            # self.symbol_table.pop_scope()
            pass
        elif node.statement == 'CONTINUE':
            pass

        # no return

    def visit_PrintStatement(self, node: AST.PrintStatement):
        # print('PrintStatement')
        self.visit(node.expressions)
        return None

    def visit_Expressions(self, node: AST.Expressions):
        # print('Expressions')

        types = []

        for expression in node.expressions:
            types.append(self.visit(expression))

        return types

    def visit_ReturnStatement(self, node: AST.ReturnStatement):
        # print('ReturnStatement')
        if node.expression is not None:
            return self.visit(node.expression)
        return None

    def visit_WhileLoop(self, node: AST.WhileLoop):
        # print('WhileLoop')
        self.symbol_table.push_scope(ScopeName.WHILE)

        expression_t = self.visit(node.expression)
        if expression_t != Bool_t and expression_t is not None:
            print('At line:', node.expression.lineno, '|',
                  f'WhileLoop expression must return Bool, not {expression_t}.')
        if node.instruction is not None:
            self.visit(node.instruction)

        self.symbol_table.pop_scope()
        # no return

    def visit_ForLoop(self, node: AST.ForLoop):
        # print('ForLoop')
        self.symbol_table.push_scope(ScopeName.FOR)

        # we do not check for name shadowing
        # iterator = self.visit(node.variable)

        # these two below should be of Integer type
        # & we need to check for it, because if they were passed as ID
        # scanner did not verify their type
        left = self.visit(node.range_value_left)
        right = self.visit(node.range_value_right)

        # iterator should be of Integer or Range/Slice type?
        self.symbol_table.put(node.variable.name, VariableSymbol(
            node.variable.name, Integer_t))

        # print(left, right)
        if left != Integer_t and left is not None:
            print('At line:', node.range_value_left.lineno,
                  '|', "Range boundary must be of integer type")
        if right != Integer_t and right is not None:
            print('At line:', node.range_value_right.lineno,
                  '|', "Range boundary must be of integer type")

        self.visit(node.instruction)
        self.symbol_table.pop_scope()
        # no return

    def visit_Slice(self, node: AST.Slice):
        # print('Slice', node.name, self.visit(node.vector))
        return node.name, self.visit(node.vector)
