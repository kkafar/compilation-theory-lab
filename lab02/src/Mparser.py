#!/usr/bin/python

import scanner
import ply.yacc as yacc


tokens = scanner.tokens

precedence = (
    # to fill ...
    ("nonassoc", 'IF'),
    ("nonassoc", 'ELSE'),
    ("left", '+', '-'),
    ("left", '*', '/'),
    ("left", 'MATRIX_PLUS', 'MATRIX_SUB'),
    ("left", 'MATRIX_MUL', 'MATRIX_DIV'),
    # to fill ...
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(
            p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instructions_opt"""


def p_instruction_opt_1(p):
    """instructions_opt : instructions """


def p_instruction_opt_2(p):
    """instructions_opt : """


def p_instructions(p):
    """
        instructions : instructions instruction
                    | instruction
    """


def p_instruction(p):
    """
        instruction : assignment ';'
    """


def p_assignment(p):
    """
        assignment : assign_id '=' expression
                    | assign_id MUL_ASSIGN expression
                    | assign_id DIV_ASSIGN expression
                    | assign_id PLUS_ASSIGN expression
                    | assign_id SUB_ASSIGN expression
    """


def p_assign_id(p):
    """
        assign_id : ID
                  | ID vector
    """


def p_expression(p):
    """expression : expression_binop
                  | expression_relop
                  | expression_unary
                  | matrix_funcs
                  | constant
                  | ID
                  | matrix
                  | '(' expression ')'
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
    """expression_relop : expression RELOP_EQ expression
                | expression RELOP_GT expression
                | expression RELOP_LT expression
                | expression RELOP_GE expression
                | expression RELOP_LE expression
                | expression RELOP_NE expression
    """


def p_expression_unary(p):
    """expression_unary : '-' expression
                | expression '\\''
    """


def p_matrix_funcs(p):
    """
        matrix_funcs : ZEROS '(' DT_INTEGER ')'
                    | ONES '(' DT_INTEGER ')'
                    | EYE '(' DT_INTEGER ')'  

    """


def p_constant(p):
    """
        constant : DT_STRING
                | number
    """


def p_matrix(p):
    """
        matrix : '[' vectors ']'

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
                | 
    """


def p_number(p):
    """
        number : DT_INTEGER 
               | DT_FLOAT
    """


# to finish the grammar
# ....


parser = yacc.yacc()
