import ply.lex as lex

tokens = (
    'LINE',
)

def t_COMMENT(t):
    r"\#.*"

def t_LINE(t):
    r"[^\n]+"
    return t

def t_newline(t):
    r'\n'
    t.type = 'NEWLINE'
    t.lineno += 1
    return t

def t_error(t):
    print("Parsing Error !")

lexer = lex.lex()

