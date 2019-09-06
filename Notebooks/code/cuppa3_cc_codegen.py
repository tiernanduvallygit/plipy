from grammar_stuff import assert_match

# codegen: this is the code generator for our Cuppa3 compiler

# NOTE: this code generator does not need access to the symbol table,
#       the abstraction level of the AST has been lowered already to the level
#       of the abstract machine code


#########################################################################
# The following is a bit of a hack: we use this global variable to broadcast
# the frame size of a function definition to all the statements within
# the function body -- the return statement needs this information in order
# to generate the proper instructions.
frame_size = None

#########################################################################
def push_args(args):
    # args can either be a ('seq', item, rest) node or a ('nil',) node.

    if args[0] == 'nil':
        return []

    else:
        # unpack the args
        (SEQ, exp_tree, rest) = args
        
        code = push_args(rest)
        
        (ecode, eloc) = walk(exp_tree)
        
        code += ecode
        code += [('pushv', eloc)]
        
        return code

#########################################################################
def pop_args(args):
    # args can either be a ('seq', item, rest) node or a ('nil',) node.

    if args[0] == 'nil':
        return []

    else:
        # unpack the args
        (SEQ, _, rest) = args
        
        code = pop_args(rest)
        code += [('popv',)]
        
        return code

#########################################################################
def init_formal_args(formal_args, ix, frame_size):
    # formal_args can either be a ('seq', item, rest) node or a ('nil',) node.
    
    if formal_args[0] == 'nil':
        return []

    else:
        # unpack the args
        (SEQ, sym, rest) = formal_args

        offset = str((0 if not ix else -ix) - frame_size - 1)
        code = [('store', sym, '%tsx['+offset+']')]
        
        return code + init_formal_args(rest, ix+1, frame_size)

#########################################################################
# node functions
#########################################################################
def seq(node):

    (SEQ, s1, s2) = node
    assert_match(SEQ, 'seq')
    
    stmt = walk(s1)
    lst = walk(s2)

    return stmt + lst

#########################################################################
def nil(node):
    
    (NIL,) = node
    assert_match(NIL, 'nil')
    
    return []
    
#########################################################################
def fundef_stmt(node):
    global frame_size

    (FUNDEF, name, formal_arglist, body, f_frame_size) = node
    assert_match(FUNDEF, 'fundef')

    frame_size = f_frame_size
    ignore_label = label()
    
    code = [('jump', ignore_label)]
    code += [('#',' ')]
    code += [('#','Start of function ' + name)]
    code += [('#',' ')]
    code += [(name + ':',)]
    code += [('pushf', str(frame_size))]
    code += init_formal_args(formal_arglist, 0, frame_size)
    code += walk(body)
    code += [('popf', str(frame_size))]
    code += [('return',)]
    code += [('#',' ')]
    code += [('#','End of function ' + name)]
    code += [('#',' ')]
    code += [(ignore_label + ':',)]
    code += [('noop',)]

    frame_size = None

    return code

#########################################################################
def call_stmt(node):
    
    (CALLSTMT, name, actual_args) = node
    assert_match(CALLSTMT, 'callstmt')

    code = push_args(actual_args)
    code += [('call', name)]
    code += pop_args(actual_args)

    return code

#########################################################################
def return_stmt(node):
    global frame_size

    try: # try return without exp
        (RETURN, (NIL,)) = node
        assert_match(RETURN, 'return')
        assert_match(NIL, 'nil')
    
        code = [('popf', str(frame_size))]
        code += [('return',)]
    
        return code

    except ValueError: # return with exp
        (RETURN, exp) = node
        assert_match(RETURN, 'return')
        
        (code, loc) = walk(exp)
        
        code += [('store', '%rvx', loc)]
        code += [('popf', str(frame_size))]
        code += [('return',)]
        
        return code

#########################################################################
def assign_stmt(node):

    (ASSIGN, name, exp) = node
    assert_match(ASSIGN, 'assign')
    
    (code, loc) = walk(exp)
    code += [('store', name, loc)]
    
    return code

#########################################################################
def get_stmt(node):

    (GET, name) = node
    assert_match(GET, 'get')

    code = [('input', name)]

    return code

#########################################################################
def put_stmt(node):

    (PUT, exp) = node
    assert_match(PUT, 'put')
    
    (code, loc) = walk(exp)
    code += [('print', loc)]

    return code

#########################################################################
def while_stmt(node):
    
    (WHILE, cond, body) = node
    assert_match(WHILE, 'while')
    
    top_label = label()
    bottom_label = label()
    (cond_code, cond_loc) = walk(cond)
    body_code = walk(body)

    code = [(top_label + ':',)]
    code += cond_code
    code += [('jumpF', cond_loc, bottom_label)]
    code += body_code
    code += [('jump', top_label)]
    code += [(bottom_label + ':',)]
    code += [('noop',)]

    return code

#########################################################################
def if_stmt(node):

    try: # try the if-then pattern
        (IF, cond, s1, (NIL,)) = node
        assert_match(IF, 'if')
        assert_match(NIL, 'nil')
    
    except ValueError: # pattern didn't match
        # try the if-then-else pattern
        (IF, cond, s1, s2) = node
        assert_match(IF, 'if')
        
        else_label = label()
        end_label = label()
        (cond_code, cond_loc) = walk(cond)
        stmt1_code = walk(s1)
        stmt2_code = walk(s2)

        code = cond_code
        code += [('jumpF', cond_loc, else_label)]
        code += stmt1_code
        code += [('jump', end_label)]
        code += [(else_label + ':',)]
        code += stmt2_code
        code += [(end_label + ':',)]
        code += [('noop',)]

        return code

    else:
        end_label = label();
        (cond_code, cond_loc) = walk(cond)
        stmt1_code = walk(s1)

        code = cond_code
        code = [('jumpF', cond_loc, end_label)]
        code += stmt1_code
        code += [(end_label + ':',)]
        code += [('noop',)]

        return code

#########################################################################
def block_stmt(node):

    (BLOCK, s) = node
    assert_match(BLOCK, 'block')

    code = walk(s)
    
    return code

#########################################################################
def binop_exp(node):

    (OP, temp, c1, c2) = node
    if OP not in ['+', '-', '*', '/', '==', '<=']:
        raise ValueError("pattern match failed on " + OP)
    
    (lcode, lloc) = walk(c1)
    (rcode, rloc) = walk(c2)

    code = lcode + rcode
    code += [('store', temp, '(' + OP + ' ' + lloc + ' ' + rloc + ')')]
    loc = temp

    return (code, loc)

#########################################################################
def call_exp(node):

    (CALLEXP, temp, name, actual_args) = node
    assert_match(CALLEXP, 'callexp')

    code = push_args(actual_args)
    code += [('call', name)]
    code += pop_args(actual_args)
    code += [('store', temp, '%rvx')]
    loc = temp

    return (code, loc)

#########################################################################
def integer_exp(node):

    (INTEGER, value) = node
    assert_match(INTEGER, 'integer')

    code = []
    loc = str(value)
    
    return (code, loc)

#########################################################################
def id_exp(node):
    
    (ID, name) = node
    assert_match(ID, 'id')
    
    code = []
    loc = name
    
    return (code, loc)

#########################################################################
def uminus_exp(node):
    
    (UMINUS, temp, e) = node
    assert_match(UMINUS, 'uminus')
    
    (code, loc) = walk(e)

    code += [('store', temp, '-' + loc)]
    loc = temp
    
    return (code, loc)

#########################################################################
def not_exp(node):
    
    (NOT, temp, e) = node
    assert_match(NOT, 'not')
    
    (code, loc) = walk(e)

    code += [('store', temp, '!' + loc)]
    loc = temp
    
    return (code, loc)

#########################################################################
# walk
#########################################################################
def walk(node):
    node_type = node[0]
    
    if node_type in dispatch_dict:
        node_function = dispatch_dict[node_type]
        return node_function(node)
    
    else:
        raise ValueError("walk: unknown tree node type: " + node_type)

# a dictionary to associate tree nodes with node functions
dispatch_dict = {
    'seq'     : seq,
    'nil'     : nil,
    'fundef'  : fundef_stmt,
    'callstmt': call_stmt,
    'return'  : return_stmt,
    'assign'  : assign_stmt,
    'get'     : get_stmt,
    'put'     : put_stmt,
    'while'   : while_stmt,
    'if'      : if_stmt,
    'block'   : block_stmt,
    'callexp' : call_exp,
    'integer' : integer_exp,
    'id'      : id_exp,
    'uminus'  : uminus_exp,
    'not'     : not_exp,
    '+'       : binop_exp,
    '-'       : binop_exp,
    '*'       : binop_exp,
    '/'       : binop_exp,
    '=='      : binop_exp,
    '<='      : binop_exp

}

#########################################################################
label_id = 0

def label():
    global label_id
    s =  'L' + str(label_id)
    label_id += 1
    return s

#########################################################################

