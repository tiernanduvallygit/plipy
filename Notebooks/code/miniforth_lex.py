# Lexer for miniForth

from ply import lex

reserved = {
    'VARIABLE'  : 'VARIABLE',
    'TRUE'      : 'TRUE',
    'FALSE'     : 'FALSE',
    'AND'       : 'AND',
    'OR'        : 'OR',
    'INVERT'    : 'INVERT',
    'DUP'       : 'DUP',
    'IF'        : 'IF',
    'ELSE'      : 'ELSE',
    'THEN'      : 'THEN',
    'BEGIN'     : 'BEGIN',
    'WHILE'     : 'WHILE',
    'REPEAT'    : 'REPEAT',
}

literals = ['+', '-', '*', '/', '=', '<', '>', '.', '!', '@']

tokens = ['ID', 'NUMBER', 'STRING'] + list(reserved.values())

t_ignore = ' \t'

#def t_NONE(_):
    # dummy token to make lex happy
#    pass

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_NUMBER(t):
    r'[0-9]+'
    return t

def t_STRING(t):
    r'\"[^\"]*\"'
    t.value = t.value[1:-1] # strip the quotes
    return t

def t_COMMENT(t):
    r'~.*'
    pass

def t_NEWLINE(t):
    r'\n'
    pass

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex(debug=0)
