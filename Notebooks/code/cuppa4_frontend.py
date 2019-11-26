# Specification of the Cuppa4 Frontend

from ply import yacc
from cuppa4_lex import tokens, lexer
from cuppa4_state import state

#########################################################################
# set precedence and associativity
# NOTE: all operators need to have tokens
#       so that we can put them into the precedence table
precedence = (
              ('left', 'EQ', 'LE'),
              ('left', 'PLUS', 'MINUS'),
              ('left', 'TIMES', 'DIVIDE'),
              ('right', 'UMINUS', 'NOT')
             )

#########################################################################
# grammar rules with embedded actions
#########################################################################
def p_prog(p):
    '''
    program : stmt_list
    '''
    state.AST = p[1]

#########################################################################
def p_stmt_list(p):
    '''
    stmt_list : stmt stmt_list
              | empty
    '''
    if (len(p) == 3):
        p[0] = ('seq', p[1], p[2])
    else:
        p[0] = p[1]

#########################################################################
#    stmt : VOID_TYPE ID '(' opt_formal_args ')' stmt
#         | data_type ID '(' opt_formal_args ')' stmt
#         | data_type ID opt_init opt_semi
#         | ID '=' exp opt_semi
#         | GET ID opt_semi
#         | PUT exp opt_semi
#         | ID '(' opt_actual_args ')' opt_semi
#         | RETURN opt_exp opt_semi
#         | WHILE '(' exp ')' stmt
#         | IF '(' exp ')' stmt opt_else
#         | '{' stmt_list '}'

def p_stmt_1(p):
    '''
    stmt : VOID_TYPE ID '(' opt_formal_args ')' stmt
    '''
    p[0] = ('fundecl', p[1], p[2], p[4], p[6])

def p_stmt_2(p):
    '''
    stmt : data_type ID '(' opt_formal_args ')' stmt
    '''
    p[0] = ('fundecl', p[1], p[2], p[4], p[6])

def p_stmt_3(p):
    '''
    stmt : data_type ID opt_init opt_semi
    '''
    p[0] = ('scalardecl', p[1], p[2], p[3])

def p_stmt_4(p):
    '''
    stmt : ID '=' exp opt_semi
    '''
    p[0] = ('assign', p[1], p[3])

def p_stmt_5(p):
    '''
    stmt : GET ID opt_semi
    '''
    p[0] = ('get', p[2])

def p_stmt_6(p):
    '''
    stmt : PUT exp opt_semi
    '''
    p[0] = ('put', p[2])

def p_stmt_7(p):
    '''
    stmt : ID '(' opt_actual_args ')' opt_semi
    '''
    p[0] = ('callstmt', p[1], p[3])

def p_stmt_8(p):
    '''
    stmt : RETURN opt_exp opt_semi
    '''
    p[0] = ('return', p[2])

def p_stmt_9(p):
    '''
    stmt : WHILE '(' exp ')' stmt
    '''
    p[0] = ('while', p[3], p[5])

def p_stmt_10(p):
    '''
    stmt : IF '(' exp ')' stmt opt_else
    '''
    p[0] = ('if', p[3], p[5], p[6])

def p_stmt_11(p):
    '''
    stmt : '{' stmt_list '}'
    '''
    p[0] = ('block', p[2])

#########################################################################
#    data_type : INTEGER_TYPE
#              | FLOAT_TYPE
#              | STRING_TYPE
def p_data_type_1(p):
    '''
    data_type : INTEGER_TYPE
    '''
    p[0] = 'integer'

def p_data_type_2(p):
    '''
    data_type : FLOAT_TYPE
    '''
    p[0] = 'float'

def p_data_type_3(p):
    '''
    data_type :  STRING_TYPE
    '''
    p[0] = 'string'

#########################################################################
def p_opt_formal_args(p):
    '''
    opt_formal_args : formal_args
                    | empty
    '''
    p[0] = p[1]

#########################################################################
#    formal_args : data_type ID ',' formal_args
#                | data_type ID

def p_formal_args_1(p):
    '''
    formal_args : data_type ID ',' formal_args
    '''
    p[0] = ('seq', ('formalarg', p[1], p[2]), p[4])

def p_formal_args_2(p):
    '''
    formal_args : data_type ID
    '''
    p[0] = ('seq', ('formalarg', p[1], p[2]), ('nil',))

#########################################################################
def p_opt_init(p):
    '''
    opt_init : '=' exp
             | empty
    '''
    if p[1] == '=':
        p[0] = p[2]
    else:
        p[0] = p[1]

#########################################################################
def p_opt_actual_args(p):
    '''
    opt_actual_args : actual_args
                    | empty
    '''
    p[0] = p[1]

#########################################################################
def p_actual_args(p):
    '''
    actual_args : exp ',' actual_args
                | exp
    '''
    if (len(p) == 4):
        p[0] = ('seq', p[1], p[3])
    else:
        p[0] = ('seq', p[1], ('nil',))

#########################################################################
def p_opt_exp(p):
    '''
    opt_exp : exp
            | empty
    '''
    p[0] = p[1]

#########################################################################
def p_opt_else(p):
    '''
    opt_else : ELSE stmt
             | empty
    '''
    if p[1] == 'else':
        p[0] = p[2]
    else:
        p[0] = p[1]

#########################################################################
#    exp : exp PLUS exp
#        | exp MINUS exp
#        | exp TIMES exp
#        | exp DIVIDE exp
#        | exp EQ exp
#        | exp LE exp
#        | INTEGER
#        | FLOAT
#        | STRING
#        | ID
#        | ID '(' opt_actual_args ')'
#        | '(' exp ')'
#        | MINUS exp %prec UMINUS
#        | NOT exp

def p_exp_1(p):
    '''
    exp : exp PLUS exp
        | exp MINUS exp
        | exp TIMES exp
        | exp DIVIDE exp
        | exp EQ exp
        | exp LE exp
    '''
    p[0] = (p[2], p[1], p[3])

def p_exp_2(p):
    '''
    exp : INTEGER
    '''
    p[0] = ('integer', int(p[1]))

def p_exp_3(p):
    '''
    exp : FLOAT
    '''
    p[0] = ('float', float(p[1]))

def p_exp_4(p):
    '''
    exp : STRING
    '''
    p[0] = ('string', p[1])

def p_exp_5(p):
    '''
    exp : ID
    '''
    p[0] = ('id', p[1])

def p_exp_6(p):
    '''
    exp : ID '(' opt_actual_args ')'
    '''
    p[0] = ('callexp', p[1], p[3])

def p_exp_7(p):
    '''
    exp : '(' exp ')'
    '''
    p[0] = p[2]

def p_exp_8(p):
    '''
    exp : MINUS exp %prec UMINUS
    '''
    p[0] = ('uminus', p[2])

def p_exp_9(p):
    '''
    exp : NOT exp
    '''
    p[0] = ('not', p[2])

#########################################################################
def p_opt_semi(p):
    '''
    opt_semi : ';'
             | empty
    '''
    pass

#########################################################################
def p_empty(p):
    '''
    empty :
    '''
    p[0] = ('nil',)

#########################################################################
def p_error(t):
    print("Syntax error at '%s'" % t.value)

#########################################################################
# build the parser
#########################################################################
parser = yacc.yacc(debug=False,tabmodule='cuppa4parsetab')
