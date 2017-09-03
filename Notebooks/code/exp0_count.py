from ply import yacc
from exp0_lex import tokens, lexer

count = 0

def p_prog(_):
    '''
    prog : stmt prog
    '''
    pass

def p_prog_empty(_):
    '''
    prog : empty
    '''
    print("count = {}".format(count))

def p_stmt(_):
    '''
    stmt : 'p' exp ';'
         | 's' var exp ';'
    '''
    pass
         
def p_exp(_):
    '''
    exp : '+' exp exp
        | '-' exp exp
        | '(' exp ')'
        | num
    '''
    pass

def p_exp_var(_):
    '''
    exp : var
    '''
    global count
    count += 1

def p_var(_):
    '''
    var : 'x' 
        | 'y' 
        | 'z'
    '''
    pass
        
def p_num(_):
    '''
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
    '''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(t):
    print("Syntax error at '%s'" % t.value)

def init_count():
    global count
    count = 0

parser = yacc.yacc(debug=False, tabmodule='exp0countparsetab')
