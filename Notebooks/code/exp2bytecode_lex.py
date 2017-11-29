# Lexer for Exp2bytecode

from ply import lex

reserved = {
    'print' : 'PRINT',
    'input' : 'INPUT',
    'store' : 'STORE',
    'jumpT' : 'JUMPT',
    'jumpF' : 'JUMPF',
    'jump'  : 'JUMP',
    'call'  : 'CALL',
    'return': 'RETURN',
    'pushv' : 'PUSHV',
    'popv'  : 'POPV',
    'pushf' : 'PUSHF',
    'popf'  : 'POPF',
    'stop'  : 'STOP',
    'noop'  : 'NOOP'
}

literals = ['!',':',';','+','-','*','/','(',')','[',']']

tokens = ['NAME','NUMBER','EQ','LE','RVX','TSX','STRING'] +\
    list(reserved.values())

t_EQ = '=='
t_LE = '<='
t_RVX = '%rvx'
t_TSX = '%tsx'
t_ignore = ' \t'

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9$]*'
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\".*\"'
    t.value = t.value[1:-1] # strip the quotes
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
lexer = lex.lex(debug=0)
