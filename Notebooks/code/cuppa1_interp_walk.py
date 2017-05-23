from cuppa1_state import state
from grammar_stuff import assert_match

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
    
    value = walk(exp)
    state.symbol_table[name] = value

#########################################################################
def get_stmt(t):

    (GET, name) = t
    assert_match(GET, 'get')

    s = input("Value for " + name + '? ')
    
    try:
        value = int(s)
    except ValueError:
        raise ValueError("expected an integer value for " + name)
    
    state.symbol_table[name] = value

#########################################################################
def put_stmt(t):

    (PUT, exp) = t
    assert_match(PUT, 'put')
    
    value = walk(exp)
    print("> {}".format(value))

#########################################################################
def while_stmt(t):

    (WHILE, cond, body) = t
    assert_match(WHILE, 'while')
    
    value = walk(cond)
    while value != 0:
        walk(body)
        value = walk(cond)

#########################################################################
def if_stmt(t):
    
    try: # try the if-then pattern
        (IF, cond, s1, (NIL,)) = t
        assert_match(IF, 'if')
        assert_match(NIL, 'nil')

    except ValueError: # pattern didn't match
        try: # try if-then-else pattern
            (IF, cond, s1, s2) = t
            assert_match(IF, 'if')

        except ValueError:
            raise ValueError("walk: pattern match failed in 'if'")

        else:
            value = walk(cond)
            if value != 0:
                walk(s1)
            else:
                walk(s2)
            return
 
    else:
        value = walk(cond)
        if value != 0:
            walk(s1)
        return

#########################################################################
def block_stmt(t):
    
    (BLOCK, s) = t
    assert_match(BLOCK, 'block')
    
    walk(s)

#########################################################################
def plus_exp(t):
    
    (PLUS,c1,c2) = t
    assert_match(PLUS, '+')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return v1 + v2

#########################################################################
def minus_exp(t):
    
    (MINUS,c1,c2) = t
    assert_match(MINUS, '-')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return v1 - v2

#########################################################################
def times_exp(t):
    
    (TIMES,c1,c2) = t
    assert_match(TIMES, '*')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return v1 * v2

#########################################################################
def divide_exp(t):
    
    (DIVIDE,c1,c2) = t
    assert_match(DIVIDE, '/')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return v1 / v2

#########################################################################
def eq_exp(t):
    
    (EQ,c1,c2) = t
    assert_match(EQ, '==')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return v1 == v2

#########################################################################
def le_exp(t):
    
    (LE,c1,c2) = t
    assert_match(LE, '<=')
    
    v1 = walk(c1)
    v2 = walk(c2)
    
    return v1 <= v2

#########################################################################
def integer_exp(t):

    (INTEGER, value) = t
    assert_match(INTEGER, 'integer')
    
    return value

#########################################################################
def id_exp(t):
    
    (ID, name) = t
    assert_match(ID, 'id')
    
    return state.symbol_table.get(name, 0)

#########################################################################
def uminus_exp(t):
    
    (UMINUS, e) = t
    assert_match(UMINUS, 'uminus')
    
    val = walk(e)
    return - val

#########################################################################
# walk
#########################################################################
def walk(t):
    if t[0] in walk_dict:
        f = walk_dict[t[0]]
        return f(t)
    else:
        raise ValueError("walk: unknown tree node type" + t[0])

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
    'integer' : integer_exp,
    'id'      : id_exp,
    '+'       : plus_exp,
    '-'       : minus_exp,
    '*'       : times_exp,
    '/'       : divide_exp,
    '=='      : eq_exp,
    '<='      : le_exp,
    'uminus'  : uminus_exp
}


