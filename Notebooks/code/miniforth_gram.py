# grammar for miniForth

from ply import yacc
from miniforth_lex import tokens, lexer


def p_grammar(_):
    '''
 prog : cmds

 cmds : cmd cmds
      | empty

 cmd : dictionarycmd
     | computecmd

 dictionarycmd : VARIABLE ID

 computecmds : computecmd computecmds
            |  empty

 computecmd : NUMBER
            | STRING
            | TRUE
            | FALSE
            | ID
            | '+'
            | '-'
            | '*'
            | '/'
            | AND
            | OR
            | INVERT
            | '='
            | '<'
            | '>'
            | '.'
            | '!'
            | '@'
            | DUP
            | IF computecmds else_opt THEN
            | BEGIN computecmds WHILE computecmds REPEAT

else_opt : ELSE computecmds
         |  empty
    '''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(_):
    print("Syntax error")

### build the parser
parser = yacc.yacc()
