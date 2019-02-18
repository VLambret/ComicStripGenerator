import ply.lex as lex

tokens = (
    'EOL',
    'COMMENT',
    'BACKGROUND',
    'IMAGE_NAME',
    'VALUE',
    'KEY',
    'COLON',
    'UNKNOWN_LINE',
)

def t_EOL(t):
    r"\n"
    print(t)
    return t

def t_COMMENT(t):
    r"""\#[^\n]*"""
    print(t)
    t.value = []

def t_BACKGROUND(t):
    r"""\@[^\n]+\.png"""
    print(t)
    t.value = t.value
    return t

def t_IMAGE_NAME(t):
    r"""[^\n \t]+\.png"""
    print(t)
    t.value = t.value
    return t

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
    r""".+"""
    print(t)
    return t

def t_UNKNOWN_LINE(t):
    r"^[^\n]+"
    print(t)
    return t

def t_error(t):
    print(t)

lexer = lex.lex()

