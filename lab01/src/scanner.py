import ply.lex as lex

tokens = (
    'ID',
    'PLUS',
    'SUB',
    'MUL',
    'DIV',
    'MATRIX_PLUS',
    'MATRIX_SUB',
    'MATRIX_MUL',
    'MATRIX_DIV',
    'MATRIX_TRANSPOSE',
    'ASSIGN',
    'PLUS_ASSIGN',
    'SUB_ASSIGN',
    'MUL_ASSIGN',
    'DIV_ASSIGN',
    'BRACE_ROUND_R',
    'BRACE_ROUND_L',
    'BRACE_SQARE_L',
    'BRACE_SQARE_R',
    'BRACE_CURLY_R',
    'BRACE_CURLY_L',
    'RELOP_GT',
    'RELOP_LT',
    'RELOP_LE',
    'RELOP_GE',
    'RELOP_NE',
    'RELOP_EQ',
    'RANGE',
    'SEPARATOR',
    'END_OF_STATEMENT',
    'IF',
    "ELSE",
    'FOR',
    "WHILE",
    "BREAK",
    "CONTINUE",
    "RETURN",
    "EYE",
    "ZEROS",
    "ONES",
    "PRINT",
    "COMMENT",
    "DT_INTEGER",
    "DT_FLOAT",
    "DT_STRING",
)

t_PLUS              = r'\+'
t_SUB               = r'-'
t_MUL               = r'\*'
t_DIV               = r'/'
t_MATRIX_PLUS       = r'\.\+'
t_MATRIX_SUB        = r'\.-'
t_MATRIX_MUL        = r'\.\*'
t_MATRIX_DIV        = r'\./'
t_ASSIGN            = r'='
t_PLUS_ASSIGN       = r'\+='
t_SUB_ASSIGN        = r'-='
t_MUL_ASSIGN        = r'\*='
t_DIV_ASSIGN        = r'/='
t_BRACE_ROUND_R     = r'\)'
t_BRACE_ROUND_L     = r'\('
t_BRACE_SQARE_R     = r'\]'
t_BRACE_SQARE_L     = r'\['
t_BRACE_CURLY_R     = r'\}'
t_BRACE_CURLY_L     = r'\{'
t_RELOP_GT          = r'>'
t_RELOP_LT          = r'<'
t_RELOP_GE          = r'>='
t_RELOP_LE          = r'<='
t_RELOP_NE          = r'!='
t_RELOP_EQ          = r'=='
t_RANGE             = r':'
t_MATRIX_TRANSPOSE  = r"'"
t_SEPARATOR         = r','
t_END_OF_STATEMENT  = r';'
t_IF                = r'if'
t_ELSE              = r'else'
t_FOR               = r'for'
t_WHILE             = r'while'
t_BREAK             = r'break'
t_CONTINUE          = r'continue'
t_RETURN            = r'return'
t_EYE               = r'eye'
t_ZEROS             = r'zeros'
t_ONES              = r'ones'
t_PRINT             = r'print'
t_ignore            = ' \t'

def t_DT_INTEGER(t):
    r'[-+]?[0-9]+'
    t.value = int(t.value)
    return t

def t_DT_FLOAT(t):
    r'\d+(\.\d+)?([eE][+-]?\d+)?'
    t.value = float(t.value)
    return t

def t_DT_STRING(t):
    r'((".*")|(\'.*\'))'
    t.value = str(t.value)
    return t
    
def t_ID(t):
    r'[a-zA-Z_][\w\d_]*'
    t.value = str(t.value)
    return t

def t_COMMENT(t):
    r'\#.*'
    # ignore

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_error(t):
    print(f"{t.value}")
    t.lexer.skip(1)

# TRZEBA DODAC OBSLUGE KOMENTARZY

lexer = lex.lex()
