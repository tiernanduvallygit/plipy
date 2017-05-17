### a parser for Simple1 builds abstract syntax trees based
### on the Python builtin tuples.  a tree node is of the format
### (<node type>, <children>,...)

from ply import yacc
from cuppa1_lex import tokens, lexer

# set precedence and associativity
precedence = (
               ('left', 'EQ','LE'),
               ('left', '+','-'),
               ('left', '*','/'),
               ('right','UMINUS')
)

########## grammar #############

def p_grammar(_):
    '''
    program : stmt_list
    stmt_list : stmt stmt_list
              | stmt
    stmt : ID EQUALS exp
         | GET ID
         | PUT exp
         | WHILE LPAREN exp RPAREN stmt
         | IF LPAREN exp RPAREN stmt else_part
         | LBRACE stmt_list RBRACE
    else_part : ELSE stmt
              |
    exp : exp PLUS exp
           | exp MINUS exp
           | exp TIMES exp
           | exp DIVIDE exp
           | exp EQ exp
           | exp LE exp
           | INTEGER
           | ID
           | LPAREN exp RPAREN
           | MINUS exp %prec UMINUS
    '''
    pass

### build the parser
parser = yacc.yacc()




       
   
  
            






