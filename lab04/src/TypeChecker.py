#!/usr/bin/python

import AST
import SymbolTable as st

numeric = {'int', 'float'}
symbol_table = st.SymbolTable()

std_operation_type_table = {
    'int': {
        'float': 'float',
        'int': 'int'
    },
    'float': {
        'float': 'float',
        'int': 'float'
    }
}

type_table = {
    op: std_operation_type_table for op in {'+', '-', '*', '/'}
}


class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)


    def generic_visit(self, node):        # Called if no explicit visitor function exists for a node.
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
    #def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)



class TypeChecker(NodeVisitor):


    def visit_Program(self, node):
        self.visit(node.instructions)

    
    def visit_Instructions(self, node):
        for instruction in node.instructions:
            self.visit(instruction)

    def visit_IntNum(self, node):
        return 'int'

    def visit_FloatNum(self, node):
        return 'float'

    def visit_StringValue(self, node):
        return 'string'
    
    def visit_Variable(self, node):
        #wyszukaj typ w tablicy w symboli?
        return node.name
    
        

    def visit_Program(self, node):
        self.visit(node.instructions)

    def visit_BinExpr(self, node):
                                          # alternative usage,
                                          # requires definition of accept method in class Node
        type1 = self.visit(node.left)     # type1 = node.left.accept(self) 
        type2 = self.visit(node.right)    # type2 = node.right.accept(self)
        op    = node.op
        

        if op in ['+', '-', '*', '/']:
            if type1 not in ['int', 'float'] or type2 not in ['int', 'float']:
                print(f'{type1} {type2} not compatible with {op}')
            else:
                return ttype[op][type1][type2]
                

        if op in ['.+', '.-', '.*', './']:
            if type1 not in ['vector'] or type2 not in ['vector']:
                print(f'{type1} {type2} not compatible with {op}')
            else:
                return ttype[op][type1][type2]

    def visit_RelopExpr(self, node):
                                          # alternative usage,
                                          # requires definition of accept method in class Node
        type1 = self.visit(node.left)     # type1 = node.left.accept(self) 
        type2 = self.visit(node.right)    # type2 = node.right.accept(self)
        op    = node.op
        

        if type1 not in numeric or type2 not in numeric:
            print(f'{type1} {type2} not comparable')
        
        return 'bool'

    def visit_UnaryExpr(self, node):
                                          # alternative usage,
                                          # requires definition of accept method in class Node
        operator = node.operator
        operand_t  = self.visit(node.operand)

        if operator == '-':
            pass

        if operator == 'TRANSPOSE':
            if operand_t != 'vector':
                print(f'invalid operand type for transposing')
            else:
                return 'vector'
        
        if operator == '-':
            if operand_t not in numeric:
                print(f'invalid operand unary minus')
            else:
                return operand_t

    def visit_Assignment(self, node):
        op = node.op
        left_name = self.visit()
        right_t = self.visit(node.right)

        symbol_table.put(node.left.name)





                
            

 



