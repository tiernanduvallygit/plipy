from exp1_lex import lexer
from grammar_stuff import TokenStream

symbol_table = dict()
token_stream = None

def exp():
    tok = token_stream.pointer()
    
    if tok.type == '+':
        token_stream.next() # match '+'
        return exp() + exp()
    
    elif tok.type == '-':
        token_stream.next() # match '-'
        return exp() - exp()
    
    elif tok.type == '(':
        token_stream.next() # match '('
        val = exp()
        token_stream.next() # match ')'
        return val
    
    elif tok.type == 'NAME':
        return var()
    
    elif tok.type == 'NUMBER':
        return num()
    
    else:
        raise SyntaxError('unexpected symbol {} while parsing'.format(tok.value))

def var():
    tok = token_stream.pointer()
    
    if tok.type == 'NAME':
        token_stream.next()
        return symbol_table.get(tok.value, 0) # return 0 if not found
    
    else:
        raise SyntaxError('unexpected symbol {} while parsing'.format(tok.value))

def num():
    tok = token_stream.pointer()
    
    if tok.type == 'NUMBER':
        token_stream.next()
        return tok.value
    
    else:
        raise SyntaxError('unexpected symbol {} while parsing'.format(tok.value))

def stmt():
    tok = token_stream.pointer()
    
    if tok.type == 'PRINT':
        token_stream.next() # match PRINT
        print("> {}".format(exp()))
        token_stream.next() # match ;
        return None
    
    elif tok.type == 'STORE':
        token_stream.next() # match STORE
        name = lvar() # not var()!
        val = exp()
        symbol_table[name] = val
        token_stream.next() # match ;
        return None
    
    else:
        raise SyntaxError('unexpected symbol {} while parsing'.format(tok.value))

def lvar():
    tok = token_stream.pointer()
    
    if tok.type == 'NAME':
        token_stream.next()
        return tok.value # return var name
    
    else:
        raise SyntaxError('unexpected symbol {} while parsing'.format(tok.value))

def stmt_list():
    while not token_stream.end_of_file():
        stmt()
    return None

def exp1_rinterp(input_stream = None):
    'driver for our recursive descent Exp1 interpreter.'
    
    global token_stream
    global symbol_table
    
    if not input_stream:
        input_stream = input("exp1 > ")
    
    token_stream = TokenStream(lexer, input_stream)
    symbol_table = dict()
    
    stmt_list()


