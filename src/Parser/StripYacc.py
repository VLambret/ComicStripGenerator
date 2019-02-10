import ply.yacc as yacc

from Parser.StripLex import tokens
from Model.Strip import Strip

def p_strip(p):
    """strip : empty"""
    print("Creating new strip")
    p[0] = Strip()

def p_empty(p):
    """empty : """

parser = yacc.yacc()

