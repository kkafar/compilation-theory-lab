#!/usr/bin/python

import scanner
import ply.yacc as yacc


tokens = scanner.tokens

precedence = (
   # to fill ...
   ("nonassoc", 'IFX'),
   ("nonassoc", 'ELSE'),
   ("left", '+', '-'),
   ("left", '*', '/'),
   ("left", 'MATRIX_PLUS', 'MATRIX_SUB'),
   ("left", 'MATRIX_MUL', 'MATRIX_DIV'),
   # to fill ...
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : expressions_opt"""

def p_expressions_opt_1(p):
    """expressions_opt : expressions """

def p_expressions_opt_2(p):
    """expressions_opt : """

def p_expressions_1(p):
    """expressions : expressions expression """

def p_expressions_2(p):
    """expressions : expression """


def p_expression(p):
    """expression : expression_binop
                  | expression_relop
                  | expression_unary
                  | matrix_init
                  | 
                  """

def p_expression_binop(p):
    """expression_binop : expression '+' expression
                | expression '-' expression
                | expression '*' expression
                | expression '/' expression
                | expression MATRIX_PLUS expression
                | expression MATRIX_SUB expression
                | expression MATRIX_MUL expression
                | expression MATRIX_DIV expression
    """

def p_expression_relop(p):
    """expression : expression RELOP_EQ expression
                | expression RELOP_GT expression
                | expression RELOP_LT expression
                | expression RELOP_GE expression
                | expression RELOP_LE expression
                | expression RELOP_NE expression
    """

def p_expression_unary(p):
    """expression : '-' expression
                | expression '\\''
    """

def p_matrix_init(p):
    """
        instruction : ID '=' '[' vectors ']'
    
    """

def p_vectors(p):
    """ vectors : vector 
                | vectors ',' vector
    """
    

def p_vector(p):
    """
        vector : '[' numbers ']'
    """

def p_numbers(p):
    """
        numbers : numbers ',' number 
                | number
    """

def p_number(p):
    """
        number : INTEGER 
               | FLOAT
    """





# to finish the grammar
# ....


    


parser = yacc.yacc()
