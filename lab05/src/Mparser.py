#!/usr/bin/python

import scanner
import ply.yacc as yacc
import AST

error_flag = False

tokens = scanner.tokens

precedence = (
    ("nonassoc", 'IFX'),
    ("nonassoc", 'ELSE'),
    ("nonassoc", 'RELOP_EQ', 'RELOP_NE', 'RELOP_GT',
     'RELOP_LT', 'RELOP_GE', 'RELOP_LE'),
    ("left", '+', '-'),

    ("left", 'MATRIX_PLUS', 'MATRIX_SUB'),
    ("left", '*', '/'),
    ("left", 'MATRIX_MUL', 'MATRIX_DIV'),
    ("right", 'UMINUS'),
    ("left", '\'')
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(
            p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")

    global error_flag
    error_flag = True


def p_program(p):
    """program : instructions_opt"""
    p[0] = p[1]


def p_empty(p):
    """
        empty : 
    """
    p[0] = AST.Empty()


def p_instruction_opt_1(p):
    """instructions_opt : instructions """
    p[0] = AST.Program(p[1])


def p_instruction_opt_2(p):
    """instructions_opt : empty """
    p[0] = AST.Program()


def p_instructions(p):
    """
        instructions : instructions instruction
    """

    p[0] = p[1]
    p[0].instructions += [p[2]]


def p_instructions_2(p):
    """
        instructions : instruction
    """

    if isinstance(p[1], AST.Instructions):
        p[0] = p[1]
    else:
        p[0] = AST.Instructions(p[1])


def p_instruction(p):
    """
        instruction : assignment
                    | conditional_statement
                    | print_statement
                    | jump_statement
                    | return_statement
                    | while_loop
                    | for_loop
                    | instruction_block
    """

    p[0] = p[1]


def p_instruction_block(p):
    """
        instruction_block : '{' instructions '}'
    """
    p[0] = p[2]


def p_assignment(p):
    """
        assignment : assign_id '=' expression ';'
                    | assign_id MUL_ASSIGN expression ';'
                    | assign_id DIV_ASSIGN expression ';'
                    | assign_id PLUS_ASSIGN expression ';'
                    | assign_id SUB_ASSIGN expression ';'
    """

    p[0] = AST.Assignment(p[2], p[1], p[3])
    p[0].lineno = p.lineno(2)


def p_assign_id(p):
    """
        assign_id : ID
    """
    p[0] = AST.Variable(p[1])
    p[0].lineno = p.lineno(1)


def p_assign_slice(p):
    """
        assign_id : slice
    """
    p[0] = p[1]
    p[0].lineno = p.lineno(1)


def p_slice(p):
    """
        slice : ID slice_vector
    """

    p[0] = AST.Slice(p[1], p[2])
    p[0].lineno = p.lineno(1)


def p_slice_vector(p):
    '''
        slice_vector : '[' expression_list ']'
    '''
    p[0] = AST.SliceVector(p[2].expressions)
    p[0].lineno = p.lineno(1)


def p_slice_vector2(p):
    '''
        slice_vector : '[' range ']'
    '''
    p[0] = AST.SliceVector([p[2]])
    p[0].lineno = p.lineno(1)


def p_slice_vector3(p):
    '''
        slice_vector : '[' range ',' range ']'
    '''
    p[0] = AST.SliceVector([p[2], p[4]])
    p[0].lineno = p.lineno(1)


def p_expression(p):
    """expression : expression_binop
                  | expression_relop
                  | expression_unary
                  | matrix_funcs
                  | constant
                  | matrix
                  | vector
                  | slice
    """
    p[0] = p[1]


def p_expression_2(p):
    """expression : ID
    """
    p[0] = AST.Variable(p[1])
    p[0].lineno = p.lineno(1)


def p_expression_3(p):
    """expression : '(' expression ')'
    """
    p[0] = p[2]


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

    p[0] = AST.BinExpr(p[2], p[1], p[3])
    p[0].lineno = p.lineno(2)


def p_expression_relop(p):
    """expression_relop : expression RELOP_EQ expression
                | expression RELOP_GT expression
                | expression RELOP_LT expression
                | expression RELOP_GE expression
                | expression RELOP_LE expression
                | expression RELOP_NE expression
    """
    p[0] = AST.RelopExpr(p[2], p[1], p[3])
    p[0].lineno = p.lineno(2)


def p_expression_unary(p):
    """expression_unary : '-' expression %prec UMINUS
                | expression '\\''
    """

    if p[1] == '-':
        p[0] = AST.UnaryExpr(p[1], p[2])
        p[0].lineno = p.lineno(1)
    elif p[2] == '\'':
        p[0] = AST.UnaryExpr('TRANSPOSE', p[1])
        p[0].lineno = p.lineno(2)


def p_matrix_funcs(p):
    """
        matrix_funcs : ZEROS '(' expression_list ')'
                    | ONES '(' expression_list ')'
                    | EYE '(' expression_list ')'  

    """

    p[0] = AST.Function(p[1], p[3])
    p[0].lineno = p.lineno(1)


def p_constant(p):
    """
        constant : number
    """
    p[0] = p[1]


def p_constant_str(p):
    """
        constant : DT_STRING
    """
    p[0] = AST.StringValue(p[1])
    p[0].lineno = p.lineno(1)


def p_matrix(p):
    """
        matrix : '[' vectors ']'

    """
    p[0] = p[2]
    p[0].lineno = p.lineno(1)


def p_vectors(p):
    """ vectors : vector 
    """
    p[0] = AST.Matrix(p[1])
    p[0].lineno = p.lineno(1)


def p_vectors_2(p):
    """ vectors : vectors ',' vector
    """
    p[0] = p[1]
    p[0].vectors += [p[3]]
    p[0].lineno = p.lineno(1)


def p_vector(p):
    """
        vector : '[' numbers ']'
                | '[' ']'
    """

    if len(p) == 4:
        p[0] = p[2]
        p[0].lineno = p.lineno(2)
    else:
        p[0] = AST.Vector()
        p[0].lineno = p.lineno(1)


def p_numbers(p):
    """
        numbers : numbers ',' number 
                | number
    """

    if len(p) == 4:
        p[0] = p[1]
        p[0].values += [p[3]]
    else:
        p[0] = AST.Vector(p[1])

    p[0].lineno = p.lineno(1)


def p_number_int(p):
    """
        number : DT_INTEGER 
    """

    p[0] = AST.IntNum(p[1])
    p[0].lineno = p.lineno(1)


def p_number_float(p):
    """
        number : DT_FLOAT
    """

    p[0] = AST.FloatNum(p[1])
    p[0].lineno = p.lineno(1)


def p_conditional_statement(p):
    """
        conditional_statement : IF '(' expression ')' instruction %prec IFX
                    | IF '(' expression ')' instruction ELSE instruction
    """

    if len(p) == 6:
        p[0] = AST.Conditional(p[3], p[5])
    else:
        p[0] = AST.Conditional(p[3], p[5], p[7])

    p[0].lineno = p.lineno(2)


def p_jump_statement(p):
    """
        jump_statement : BREAK ';'
                        | CONTINUE ';'
    """
    p[0] = AST.JumpStatement(p[1])
    p[0].lineno = p.lineno(1)


def p_return_statement(p):
    """
        return_statement : RETURN ';'
                        | RETURN expression ';'
    """

    if len(p) == 3:
        p[0] = AST.ReturnStatement()
    else:
        p[0] = AST.ReturnStatement(p[2])

    p[0].lineno = p.lineno(1)


def p_print_statement(p):
    """
        print_statement : PRINT expression_list ';'
    """

    p[0] = AST.PrintStatement(p[2])


def p_expression_list(p):
    """
        expression_list : expression_list ',' expression
    """
    p[0] = p[1]
    p[0].expressions += [p[3]]


def p_expression_list_2(p):
    """
        expression_list : expression
    """
    p[0] = AST.Expressions(p[1])


def p_while_loop(p):
    """
        while_loop : WHILE '(' expression ')' instruction
    """
    p[0] = AST.WhileLoop(p[3], p[5])


def p_for_loop(p):
    """
        for_loop : FOR ID '=' range instruction
    """
    p[0] = AST.ForLoop(AST.Variable(p[2]), p[4], p[5])


def p_range(p):
    """
        range : expression ':' expression
    """
    p[0] = AST.Range(p[1], p[3])
    p[0].lineno = p.lineno(2)


parser = yacc.yacc()
