from ply import yacc
from exp1_lex import tokens, lexer

def p_grammar(_):
    """
    prog : stmt_list
    
    stmt_list : stmt stmt_list
              | empty
              
    stmt : PRINT exp ';'
         | STORE var exp ';'
         
    exp : '+' exp exp
        | '-' exp exp
        | '(' exp ')'
        | var
        | num
        
    var : NAME
        
    num : NUMBER
    """
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc()
