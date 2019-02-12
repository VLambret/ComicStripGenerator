import ply.lex as lex

tokens = (
    'UNKNOWN_LINE',
    'KEY',
    'COLON',
    'CONFIG_KEY',
    'EOL',
)

def t_KEY(t):
    r"""database"""
    return t

def t_COLON(t):
    r""":"""
    return t

def t_CONFIG_KEY(t):
    r"""toto"""
    return t

def t_UNKNOWN_LINE(t):
    r"[^\n]+"
    return t

def t_EOL(t):
    r"\n"
    return t

lexer = lex.lex()

