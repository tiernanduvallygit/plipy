'''
exp2bytecode - same as exp1bytecode but with function calls and expanded IO
'''
from ply import yacc
from exp2bytecode_lex import tokens, lexer

def p_grammar(_):
    '''
    prog : instr_list

    instr_list : labeled_instr instr_list
               | empty

    labeled_instr : label_def instr

    label_def : NAME ':' 
              | empty

    instr : PRINT opt_string exp ';'
          | INPUT opt_string storable ';'
          | STORE storable exp ';'
          | JUMPT exp label ';'
          | JUMPF exp label ';'
          | JUMP label ';'
          | CALL label ';'
          | RETURN ';'
          | PUSHV exp ';'
          | POPV opt_storable ';'
          | PUSHF size ';'
          | POPF size ';'
          | STOP ';'
          | NOOP ';'
          
    opt_string : STRING
               | empty
               
    opt_storable : storable
                 | empty
                 
    size : exp

    label : NAME

    exp : '+' exp exp
        | '-' exp exp
        | '-' exp
        | '*' exp exp
        | '/' exp exp
        | EQ exp exp
        | LE exp exp
        | '!' exp
        | '(' exp ')'
        | storable
        | NUMBER
        
    storable : var
             | RVX
             | TSX opt_offset
             
    opt_offset : '[' offset ']'
               | empty
               
    offset : exp

    var : NAME
    '''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc()
