from ply import yacc
from exp0_lex import tokens, lexer

def p_grammar(_):
    """
    prog : stmt_list
    
    stmt_list : stmt stmt_list
              | empty
              
    stmt : 'p' exp ';'
         | 's' var exp ';'
         
    exp : '+' exp exp
        | '-' exp exp
        | '(' exp ')'
        | var
        | num
        
    var : 'x' 
        | 'y' 
        | 'z'
        
    num : '0' 
        | '1' 
        | '2' 
        | '3' 
        | '4' 
        | '5' 
        | '6' 
        | '7' 
        | '8' 
        | '9'
    """
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc()
