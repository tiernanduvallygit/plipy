from cuppa1_state import state
from grammar_stuff import assert_match

# this is the second pass of the pretty printer that that
# generates the output together with the warning

indent_level = 0

#########################################################################
# node functions
#########################################################################
def seq(t):

    (SEQ, s1, s2) = t
    assert_match(SEQ, 'seq')
    
    stmt = walk(s1)
    list = walk(s2)

    return stmt + list

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
    
    e = walk(exp)

    code = indent() + name + ' = ' + e
    
    if not state.symbol_table[name]:
        code += ' // *** '+ name + ' is not used ***'

    code += '\n'
    return code

#########################################################################
def get_stmt(t):

    (GET, name) = t
    assert_match(GET, 'get')

    code = indent() + 'get ' + name
    
    if not state.symbol_table[name]:
        code += ' // '+ name + ' is not used'

    code += '\n'
    return code

#########################################################################
def put_stmt(t):

    (PUT, exp) = t
    assert_match(PUT, 'put')
    
    e = walk(exp)

    code = indent() + 'put ' + e + '\n'
    return code

#########################################################################
def while_stmt(t):
    global indent_level
    
    (WHILE, cond, body) = t
    assert_match(WHILE, 'while')
    
    c = walk(cond)

    indent_level += 1
    b = walk(body)
    indent_level -= 1

    code = indent() + 'while (' + c + ')\n' + b

    return code

#########################################################################
def if_stmt(t):
    global indent_level

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
            c = walk(cond)

            indent_level += 1
            stmt1 = walk(s1)
            stmt2 = walk(s2)
            indent_level -= 1

            code = indent() + 'if (' + c + ')\n' + stmt1
            code += indent() + 'else\n' + stmt2
            return code

    else:
        c = walk(cond)

        indent_level += 1
        stmt1 = walk(s1)
        indent_level -= 1

        code = indent() + 'if (' + c + ')\n' + stmt1
        return code
    


#########################################################################
def block_stmt(t):
    global indent_level
    adjust_level = False

    (BLOCK, s) = t
    assert_match(BLOCK, 'block')

    if indent_level > 0:
        indent_level -= 1
        adjust_level = True

    indent_level += 1
    block = walk(s)
    indent_level -= 1
    
    code = indent() + '{\n' + block + indent() + '}\n'

    if adjust_level:
        indent_level += 1
    
    return code

#########################################################################
def binop_exp(t):

    (BINOP,op,c1,c2) = t
    assert_match(BINOP, 'binop')
    
    l = walk(c1)
    r = walk(c2)

    code = l + ' ' + op + ' ' + r

    return code

#########################################################################
def integer_exp(t):

    (INTEGER, value) = t
    assert_match(INTEGER, 'integer')

    return str(value)

#########################################################################
def id_exp(t):
    
    (ID, name) = t
    assert_match(ID, 'id')
    
    return name

#########################################################################
def uminus_exp(t):
    
    (UMINUS, e) = t
    assert_match(UMINUS, 'uminus')
    
    c = walk(e)

    return '-' + c

#########################################################################
# visitor walker
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


def indent():
    s = ''
    for i in range(indent_level):
        s += '   '
    return s

