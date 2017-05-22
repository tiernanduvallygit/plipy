from cuppa1_state import state
from grammar_stuff import assert_match

# this is the first pass of the pretty printer that looks at
# variable declarations

#########################################################################
# node functions
#########################################################################
def seq(t):

    (SEQ, s1, s2) = t
    assert_match(SEQ, 'seq')
    
    walk(s1)
    walk(s2)

#########################################################################
def nil(t):
    
    (NIL,) = t
    assert_match(NIL, 'nil')
    
    # do nothing!
    pass

#########################################################################
def assign_stmt(t):

    (ASSIGN, name, exp) = t
    assert_match(ASSIGN, 'assign')
    
    walk(exp)

    if name not in state.symbol_table:
        state.symbol_table[name] = False

#########################################################################
def get_stmt(t):

    (GET, name) = t
    assert_match(GET, 'get')

    if name not in state.symbol_table:
        state.symbol_table[name] = False

#########################################################################
def put_stmt(t):

    (PUT, exp) = t
    assert_match(PUT, 'put')
    
    walk(exp)

#########################################################################
def while_stmt(t):

    (WHILE, cond, body) = t
    assert_match(WHILE, 'while')
    
    walk(cond)
    walk(body)

#########################################################################
def if_stmt(t):

try: # try the if-then pattern
    (IF, cond, s1, s2) = t
    assert_match(IF, 'if')
    
    walk(cond)
    walk(s1)
    walk(s2)

#########################################################################
def block_stmt(t):

    (BLOCK, s) = t
    assert_match(BLOCK, 'block')

    walk(s)

#########################################################################
def binop_exp(t):

    (BINOP,op,c1,c2) = t
    assert_match(BINOP, 'binop')
    
    walk(c1)
    walk(c2)

#########################################################################
def integer_exp(t):

    (INTEGER, value) = t
    assert_match(INTEGER, 'integer')

#########################################################################
def id_exp(t):
    
    (ID, name) = t
    assert_match(ID, 'id')
    
    state.symbol_table[name] = True

#########################################################################
def uminus_exp(t):
    
    (UMINUS, e) = t
    assert_match(UMINUS, 'uminus')
    
    walk(e)

#########################################################################
# walk
#########################################################################
def walk(t):
    if t[0] in walk_dict:
        f = walk_dict[t[0]]
        return f(t)
    else:
        raise ValueError("walk: unknown tree node " + t[0])

# a dictionary to associate tree nodes with node functions
walk_dict = {
    'seq'     : seq,
    'nil'     : nil,
    'assign'  : assign_stmt,
    'get'     : get_stmt,
    'put'     : put_stmt,
    'while'   : while_stmt,
    'if'      : if_stmt,
    'block'   : block_stmt,
    'binop'   : binop_exp,
    'integer' : integer_exp,
    'id'      : id_exp,
    'uminus'  : uminus_exp
}


