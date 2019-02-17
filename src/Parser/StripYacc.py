import ply.yacc as yacc

import Config
from Parser.BackgroundLine import BackgroundLine
from Parser.StripLex import tokens
from Model.Strip import Strip

def p_strip(p):
    """strip : lines"""
    strip = Strip()
    modifier_list = p[1]
    if modifier_list:
        for modifier in modifier_list:
            if modifier:
                modifier.modify(strip)
    p[0] = strip

def p_lines(p):
    """lines : line EOL lines
             | line
             | empty"""
    print("len(p)=", len(p))
    if len(p) == 2:
        print("line", p[1])
        p[0] = p[1]
    elif len(p) == 4:
        print("Adding to lines", p[1])
        if p[1]:
            p[0] = p[1] + [p[3]]
        else:
            p[0] = [p[3]]
    else:
        print("UNEXPECTED P NUMBER", len(p))

def p_line(p):
    """line : COMMENT
            | config_line
            | panel
            | UNKNOWN_LINE"""
    p[0] = p[1]

def p_panel(p):
    """panel : BACKGROUND"""
    print("Creating Background")
    p[0] = BackgroundLine(p[1])

def p_config_line(p):
    """config_line : KEY COLON VALUE"""
    print("key=", p[1], " detected ! with value=", p[3])
    if p[1] == "database":
        Config.image_database = p[3]

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

