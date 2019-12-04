# Specification of the Cuppa4 Frontend

from ply import yacc
from cuppa5_lex import tokens, lexer
from cuppa5_state import state

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
#         | storable '=' exp opt_semi
#         | GET storable opt_semi
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
    p[0] = ('fundecl', (p[2],), p[1], p[4], p[6])

def p_stmt_2(p):
    '''
    stmt : data_type ID '(' opt_formal_args ')' stmt
    '''
    p[0] = ('fundecl', p[2], p[1], p[4], p[6])

def p_stmt_3(p):
    '''
    stmt : data_type ID opt_init opt_semi
    '''
    p[0] = ('decl', p[2], p[1], p[3])

def p_stmt_4(p):
    '''
    stmt : storable '=' exp opt_semi
    '''
    p[0] = ('assign', p[1], p[3])

def p_stmt_5(p):
    '''
    stmt : GET storable opt_semi
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
#    data_type : primitive_type
#              | primitive_type '[' INTEGER ']'

def p_data_type_1(p):
    '''
    data_type : primitive_type
    '''
    p[0] = p[1]

def p_data_type_2(p):
    '''
    data_type : primitive_type '[' INTEGER ']'
    '''
    p[0] = ('array-type', int(p[3]), p[1])

#########################################################################
#    primitive_type : INTEGER_TYPE
#                   | FLOAT_TYPE
#                   | STRING_TYPE

def p_primitive_type_1(p):
    '''
    primitive_type : INTEGER_TYPE
    '''
    p[0] = ('integer',)

def p_primitive_type_2(p):
    '''
    primitive_type : FLOAT_TYPE
    '''
    p[0] = ('float',)

def p_primitive_type_3(p):
    '''
    primitive_type :  STRING_TYPE
    '''
    p[0] = ('string',)

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
#    opt_init : '=' exp
#             | '=' '{' exp_list '}'
#             | empty

def p_opt_init_1(p):
    '''
    opt_init : '=' exp
    '''
    p[0] = p[2]

def p_opt_init_2(p):
    '''
    opt_init : '=' '{' exp_list '}'
    '''
    p[0] = p[3]

def p_opt_init_3(p):
    '''
    opt_init : empty
    '''
    p[0] = p[1]

#########################################################################
#    exp_list : exp ',' exp_list
#             | exp

def p_exp_list_1(p):
    '''
    exp_list : exp ',' exp_list
    '''
    p[0] = ('seq', p[1], p[3])

def p_exp_list_2(p):
    '''
    exp_list : exp
    '''
    p[0] = ('seq', p[1], ('nil',))

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
#        | storable
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
    p[0] = ('val', ('integer',), int(p[1]))

def p_exp_3(p):
    '''
    exp : FLOAT
    '''
    p[0] = ('val', ('float',), float(p[1]))

def p_exp_4(p):
    '''
    exp : STRING
    '''
    p[0] = ('val', ('string',), str(p[1]))

def p_exp_5(p):
    '''
    exp : storable
    '''
    p[0] = p[1]

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
#    storable : ID
#             | ID '[' exp ']'

def p_storable_1(p):
    '''
    storable : ID
    '''
    p[0] = ('id', p[1])

def p_storable_2(p):
    '''
    storable : ID '[' exp ']'
    '''
    p[0] = ('array-access', p[1], p[3])

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
parser = yacc.yacc(debug=False,tabmodule='cuppa5parsetab')
