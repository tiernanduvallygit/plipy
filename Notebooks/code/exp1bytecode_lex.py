# Lexer for Exp1bytecode

from ply import lex

reserved = {
    'store' : 'STORE',
    'print' : 'PRINT',
    'input' : 'INPUT',
    'jumpT' : 'JUMPT',
    'jumpF' : 'JUMPF',
    'jump'  : 'JUMP',
    'stop'  : 'STOP',
    'noop'  : 'NOOP'
}

literals = [':',';','+','-','*','/','(',')']

tokens = ['NAME','NUMBER','EQ','LE'] + list(reserved.values())

t_EQ = '='
t_LE = '=<'
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
    pass

def t_COMMENT(t):
    r'\#.*'
    pass
    
def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex()
