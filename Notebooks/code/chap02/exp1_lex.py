# Lexer for Exp1

from ply import lex

reserved = {
    'store' : 'STORE',
    'print' : 'PRINT'
}

literals = [';','+','-','(',')']

tokens = ['NAME','NUMBER','NEWLINE'] + list(reserved.values())

t_ignore = ' \t'

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex()
