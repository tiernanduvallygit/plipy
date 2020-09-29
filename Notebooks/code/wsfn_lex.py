##### Lexer for Wsfn

from ply import lex

# variables that we need to define for the lexical analysis

tokens = ['NEWLINE'] # we have to define at least one token!

literals = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
    '+',
    '-',
    '?',
    '+',
    '-',
    '(',
    ')',
    '=',
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9'
]

t_ignore = ' \t'

def t_NEWLINE(t):
    r'\n'
    pass

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex(debug=0)
