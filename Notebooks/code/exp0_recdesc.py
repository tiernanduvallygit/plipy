'''
Recursive descent grammar for Exp0:

    prog : stmt prog
         | empty
              
    stmt : 'p' exp ';'
         | 's' var exp ';'
         
    exp : '+' exp exp
        | '-' exp exp
        | '(' exp ')'
        | var
        | num
        
    var : 'x' 
        | 'y' 
        | 'z'
        
    num : '0' 
        | '1' 
        | '2' 
        | '3' 
        | '4' 
        | '5' 
        | '6' 
        | '7' 
        | '8' 
        | '9'
'''

from grammar_stuff import InputStream

def prog():
    while not I.end_of_file():
        stmt()

def stmt():
    sym = I.pointer()
    if sym == 'p':
        I.next()
        exp()
        I.next() # match the ';'
    elif sym == 's':
        I.next()
        var()
        exp()
        I.next() # match the ';'
    else:
        raise SyntaxError('unexpected symbol {} while parsing'.format(sym))
    
def exp():
    sym = I.pointer()
    if sym == '+':
        I.next()
        exp()
        exp()
    elif sym == '-':
        I.next()
        exp()
        exp()
    elif sym in ['x', 'y', 'z']:
        var()
    elif sym in ['0', '1', '2', '3', '4', '5', '6','7', '8', '9']:
        num()
    else:
        raise SyntaxError('unexpected symbol {} while parsing'.format(sym))

def var():
    sym = I.pointer()
    if sym == 'x':
        I.next()
    elif sym == 'y':
        I.next()
    elif sym == 'z':
        I.next()
    else:
        raise SyntaxError('unexpected symbol {} while parsing'.format(sym))

def num():
    sym = I.pointer()
    if sym in ['0', '1', '2', '3', '4', '5', '6','7', '8', '9']:
        I.next()
    else:
        raise SyntaxError('unexpected symbol {} while parsing'.format(sym))
    
# example test case

I = InputStream(['s', 'x', '1', ';','p', '+', 'x', '1',';'])
prog()
