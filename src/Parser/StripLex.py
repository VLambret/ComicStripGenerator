import ply.lex as lex

tokens = (
    'COMMENT',
    'UNKNOWN_LINE',
    'VALUE',
    'KEY',
    'COLON',
    'EOL',
)

def t_COMMENT(t):
    r"""^\#[^\n]*"""
    print(t)

def t_KEY(t):
    #r"""database"""
    r"""^[^:]+"""
    print(t)
    return t

def t_COLON(t):
    r""":"""
    print(t)
    return t

def t_VALUE(t):
    r"""[^:\n]+$"""
    print(t)
    return t

def t_UNKNOWN_LINE(t):
    r"[^\n]+"
    print(t)
    return t

def t_EOL(t):
    r"\n"
    print(t)
    return t

lexer = lex.lex()

