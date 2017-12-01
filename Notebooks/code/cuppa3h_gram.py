# grammar for Cuppa3h

from ply import yacc
from cuppa3h_lex import tokens, lexer

# set precedence and associativity
# NOTE: all arithmetic operators need to have tokens
#       so that we can put them into the precedence table
precedence = (
              ('left', 'EQ', 'LE'),
              ('left', 'PLUS', 'MINUS'),
              ('left', 'TIMES', 'DIVIDE'),
              ('right', 'UMINUS', 'NOT')
             )

def p_grammar(_):
    '''
    program : stmt_list

    stmt_list : stmt stmt_list
              | empty

    stmt : DECLARE ID opt_init semi
         | ID '=' exp semi
         | GET ID semi
         | PUT exp semi
         | '(' function_value ')' tuple_list semi
         | ID tuple_list semi
         | RETURN opt_exp semi
         | WHILE '(' exp ')' stmt
         | IF '(' exp ')' stmt opt_else
         | '{' stmt_list '}'

    tuple_list : '(' opt_tuple ')' tuple_list
               | '(' opt_tuple ')'
               
    opt_tuple : tuple
              | empty
    
    tuple : exp ',' tuple
          | exp
          
    opt_formal_args : formal_args
                    | empty

    formal_args : ID ',' formal_args
                | ID

    opt_init : '=' exp
             | empty
             
    opt_exp : exp
            | empty

    opt_else : ELSE stmt
             | empty
             
    semi : ';'
         | empty

    exp : exp PLUS exp
        | exp MINUS exp
        | exp TIMES exp
        | exp DIVIDE exp
        | exp EQ exp
        | exp LE exp
        | INTEGER
        | function_value
        | exp tuple_list
        | ID
        | '(' exp ')'
        | MINUS exp %prec UMINUS
        | NOT exp
        
    function_value : FUNCTION '(' opt_formal_args ')' stmt
    '''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(t):
    print("Syntax error at '%s'" % t.value)

### build the parser
parser = yacc.yacc()




       
   
  
            






