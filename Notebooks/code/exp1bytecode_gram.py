from ply import yacc
from exp1bytecode_lex import tokens, lexer

def p_grammar(_):
    '''
    prog : instr_list

    instr_list : labeled_instr instr_list
               | empty

    labeled_instr : label_def instr

    label_def : NAME ':' 
              | empty

    instr : PRINT exp ';'
          | INPUT NAME ';'
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
        | '!' exp
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
