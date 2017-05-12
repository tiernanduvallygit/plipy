from ply import yacc
from exp1bytecode_lex import tokens, lexer

def p_grammar(_):
    '''
    prog : stmt_list

    stmt_list : labeled_stmt stmt_list
              | empty

    labeled_stmt : label_def stmt

    label_def : NAME ':' 
              | empty

    stmt : PRINT exp ';'
         | STORE NAME exp ';'
         | JUMPT exp label ';'
         | JUMPF exp label ';'
         | JUMP label ';'
         | STOP ';'
         | NOOP ';'

    exp : '+' exp exp
        | '-' exp exp
        | '-' exp
        | '*' exp exp
        | '/' exp exp
        | EQ exp exp
        | LE exp exp
        | '(' exp ')'
        | var
        | NUMBER
        
    label : NAME
    var : NAME
    '''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc()
