import ply.yacc as yacc

import Config
from Parser.StripLex import tokens
from Model.Strip import Strip

def p_strip(p):
    """strip : lines"""
    p[0] = Strip()

def p_lines(p):
    """lines : line EOL lines
             | line
             | empty"""

def p_line(p):
    """line : config_line
            | unknown_line"""

def p_config_line(p):
    """config_line : KEY COLON VALUE"""
    print("key=", p[1], " detected ! with value=", p[3])
    if p[1] == "database":
        Config.image_database = p[3]

def p_unknown_line(p):
    """unknown_line : UNKNOWN_LINE"""
    print("Unknown line:", p[1])

def p_empty(p):
    """empty : """
    print("Empty !")

def p_error(p):
    if p:
        print("Syntax error at token", p.type, "with value=", p.value)
        print("p=", p)
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    else:
        print("Syntax error at EOF")

parser = yacc.yacc(debug=True)

