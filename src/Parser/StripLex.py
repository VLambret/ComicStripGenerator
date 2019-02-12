import ply.lex as lex

tokens = (
    'UNKNOWN_LINE',
    'KEY',
    'COLON',
    'CONFIG_KEY',
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


#def t_LINE(t):
#    r"[^\n]+"
#    return t
#
#def t_COMMENT(t):
#    r"\#.*"
#
#def t_LINE(t):
#    r"[^\n]+"
#    return t
#
#def t_newline(t):
#    r'\n'
#    t.type = 'NEWLINE'
#    t.lineno += 1
#    return t

#def t_error(t):
#    print("Parsing Error !")


lexer = lex.lex()

