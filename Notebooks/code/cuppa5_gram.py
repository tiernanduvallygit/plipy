# grammar for Cuppa5

from ply import yacc
from cuppa5_lex import tokens, lexer

# set precedence and associativity
# NOTE: all arithmetic operator need to have tokens
#       so that we can put them into the precedence table
precedence = (
              ('left', 'EQ', 'LE'),
              ('left', 'PLUS', 'MINUS'),
              ('left', 'TIMES', 'DIVIDE'),
              ('right', 'UMINUS', 'NOT')
             )

#          | data_type ID opt_init opt_semi


def p_grammar(_):
    '''
    program : stmt_list

    stmt_list : stmt stmt_list
              | empty

    stmt : VOID_TYPE ID '(' opt_formal_args ')' stmt
         | data_type ID '(' opt_formal_args ')' stmt
         | data_type ID opt_init opt_semi
         | storable '=' exp opt_semi
         | GET storable opt_semi
         | PUT exp opt_semi
         | ID '(' opt_actual_args ')' opt_semi
         | RETURN opt_exp opt_semi
         | WHILE '(' exp ')' stmt
         | IF '(' exp ')' stmt opt_else
         | '{' stmt_list '}'

    data_type : primitive_type
              | primitive_type '[' INTEGER ']'

    primitive_type : INTEGER_TYPE
                   | FLOAT_TYPE
                   | STRING_TYPE

    opt_formal_args : formal_args
                    | empty

    formal_args : data_type ID ',' formal_args
                | data_type ID

    opt_init : '=' exp
             | '=' '{' exp_list '}'
             | empty

    exp_list : exp ',' exp_list
             | exp

    opt_actual_args : actual_args
                    | empty

    actual_args : exp ',' actual_args
                | exp

    opt_exp : exp
            | empty

    opt_else : ELSE stmt
             | empty

    opt_semi : ';'
             | empty

    exp : exp PLUS exp
        | exp MINUS exp
        | exp TIMES exp
        | exp DIVIDE exp
        | exp EQ exp
        | exp LE exp
        | INTEGER
        | FLOAT
        | STRING
        | storable
        | ID '(' opt_actual_args ')'
        | '(' exp ')'
        | MINUS exp %prec UMINUS
        | NOT exp

    storable : ID
             | ID '[' exp ']'
    '''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(t):
    print("Syntax error at '%s'" % t.value)

### build the parser
parser = yacc.yacc(debug=True,tabmodule='cuppa5parsetab')
