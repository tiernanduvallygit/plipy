'''
Recursive descent grammar for Exp0:

    prog : stmt prog
         | ""
              
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

I = None

def set_stream(input_stream):
    global I
    I = input_stream

def prog():
    sym = I.pointer()
    if sym in ['p','s']:
        stmt()
        prog()
    elif sym == "":
        pass
    else:
        raise SyntaxError('unexpected symbol {} while parsing'.format(sym))

def stmt():
    sym = I.pointer()
    if sym == 'p':
        I.next()
        exp()
        I.match(';')
    elif sym == 's':
        I.next()
        var()
        exp()
        I.match(';') # match the ';'
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
    elif sym == '(':
        I.next()
        exp()
        I.match(')')
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

#I = InputStream(['s', 'x', '1', ';','p', '+', 'x', '1',';'])
#prog()
