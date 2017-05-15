from ply import yacc
from exp1_lex import tokens, lexer

def p_prog(p):
    "prog : stmt_list"
    print(p[1])

def p_stmt_list(p):
    "stmt_list : stmt stmt_list"
    p[0] = p[1] + p[2]

def p_stmt_list_empty(p):
    "stmt_list : empty"
    p[0] = p[1]

def p_print_stmt(p):
    "stmt : PRINT exp ';'"
    p[0] = 'print' + p[2] +';\n'

def p_store_stmt(p):
    "stmt : STORE NAME exp ';'"
    p[0] = 'store ' + p[2] + p[3] +';\n'

def p_arith_exp(p):
    """
    exp : '+' exp exp
        | '-' exp exp
        | '(' exp ')'
    """
    if p[1] == '+':
        p[0] = ' (+' + p[2] + p[3] + ')'
    elif p[1] == '-':
        p[0] = ' (-' + p[2] + p[3] + ')'
    elif p[1] == '(':
        p[0] = p[2]
    else:
        raise SyntaxError("parsing weirdness in expressions: {} !".format(p[1]))

def p_var_exp(p):
    "exp : var"
    p[0] = p[1]
    
def p_num_exp(p):
    "exp : num"
    p[0] = p[1]

def p_var(p):
    "var : NAME"
    p[0] = ' ' + p[1]

def p_num(p):
    "num : NUMBER"
    p[0] = ' ' + str(p[1])

def p_empty(p):
    "empty :"
    p[0] = ''

def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc()
