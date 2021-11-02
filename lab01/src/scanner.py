import ply.lex as lex


reserved = {
    'if'      : 'IF',
    'else'    : 'ELSE',
    'for'     : 'FOR',
    'while'   : 'WHILE',
    'break'   : 'BREAK',
    'continue': 'CONTINUE',
    'return'  : 'RETURN',
    'eye'     : 'EYE',
    'zeros'   : 'ZEROS',
    'ones'    : 'ONES',
    'print'   : 'PRINT'
}

tokens = (
    'ID',
    'MATRIX_PLUS',
    'MATRIX_SUB',
    'MATRIX_MUL',
    'MATRIX_DIV',
    'PLUS_ASSIGN',
    'SUB_ASSIGN',
    'MUL_ASSIGN',
    'DIV_ASSIGN',
    'RELOP_GT',
    'RELOP_LT',
    'RELOP_LE',
    'RELOP_GE',
    'RELOP_NE',
    'RELOP_EQ',
    "COMMENT",
    "DT_INTEGER",
    "DT_FLOAT",
    "DT_STRING"
) + tuple(reserved.values())

t_MATRIX_PLUS       = r'\.\+'
t_MATRIX_SUB        = r'\.-'
t_MATRIX_MUL        = r'\.\*'
t_MATRIX_DIV        = r'\./'
t_PLUS_ASSIGN       = r'\+='
t_SUB_ASSIGN        = r'-='
t_MUL_ASSIGN        = r'\*='
t_DIV_ASSIGN        = r'/='
t_RELOP_GT          = r'>'
t_RELOP_LT          = r'<'
t_RELOP_GE          = r'>='
t_RELOP_LE          = r'<='
t_RELOP_NE          = r'!='
t_RELOP_EQ          = r'=='

t_ignore            = ' \t'

literals = "+-*/()[]{},;:=\'"

def t_DT_FLOAT(t):
    r'[+-]?((\d+(\.\d*)?)|(\.\d+))((e|E)[+-]?\d+)?'
    t.value = float(t.value)
    return t

def t_DT_INTEGER(t):
    r'[-+]?\d+((e|E)[+-]?\d+)?'
    t.value = int(t.value)
    return t

def t_DT_STRING(t):
    r'((".*")|(\'.*\'))'
    t.value = str(t.value)[1:-1]
    return t
    
def t_ID(t):
    r'[a-zA-Z_][\w\d_]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_COMMENT(t):
    r'\#.*'
    # ignore

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()
