import ply.lex as lex

tokens = (
    'ID',
    'PLUS',
    'SUBS',
    'MUL',
    'DIV',
    'DPLUS',
    'DSUBS',
    'DMUL',
    'DDIV',
    'ASSIGN',
    'PASSIGN',
    'SUBSASSIGN',
    'MULASSIGN',
    'DIVASSIGN',
    'R_ROUND_BRACE',
    'L_ROUND_BRACE',
    'L_SQUARE_BRACE',
    'R_SQUARE_BRACE',
    'R_CURLY_BRACE',
    'L_CURLY_BRACE',
    'GT',
    'LT',
    'LE',
    'GE',
    'NE',
    'EQ',
    'RANGE',
    'TRANSPOSE',
    'COMMA',
    'SEMICOLON',
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
    "INTEGER",
    "FLOAT",
    "STRING",
    "COMMENT"
)

t_PLUS      = r'\+'
t_SUBS      = r'-'
t_MUL       = r'\*'
t_DIV       = r'/'
t_DPLUS     = r'\.\+'
t_DSUBS     = r'\.-'
t_DMUL      = r'\.\*'
t_DDIV      = r'\./'
t_ASSIGN    = r'='
t_PASSIGN   = r'\+='
t_SUBSASSIGN = r'-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='
t_R_ROUND_BRACE = r'\)'
t_L_ROUND_BRACE = r'\('
t_R_SQUARE_BRACE = r'\]'
t_L_SQUARE_BRACE = r'\['
t_R_CURLY_BRACE = r'\}'
t_L_CURLY_BRACE = r'\{'
t_GT        = r'>'
t_LT        = r'<'
t_GE        = r'>='
t_LE        = r'<='
t_NE        = r'!='
t_EQ        = r'=='
t_RANGE     = r':'
t_TRANSPOSE = r"'"
t_COMMA     = r','
t_SEMICOLON = r';'
t_IF        = r'if'
t_ELSE      = r'else'
t_FOR       = r'for'
t_WHILE     = r'while'
t_BREAK     = r'break'
t_CONTINUE  = r'continue'
t_RETURN    = r'return'
t_EYE       = r'eye'
t_ZEROS    = r'zeros'
t_ONES      = r'ones'
t_PRINT     = r'print'


def t_INTEGER(t):
    r'[-+]?[0-9]+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+(\.\d+)?([eE][+-]?\d+)?'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'((".*")|(\'.*\'))'
    t.value = str(t.value)
    return t
    
t_ignore = ' \t'

def t_error(t):
    print(f"{t.value}")
    t.lexer.skip(1)
    
def t_ID(t):
    r'[a-zA-Z_][\w\d_]*'
    t.value = str(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    # ignore
    

# TRZEBA DODAC OBSLUGE KOMENTARZY

lexer = lex.lex()

if __name__ == '__main__':

    pass