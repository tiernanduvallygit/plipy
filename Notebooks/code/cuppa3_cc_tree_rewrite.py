# A tree walker to rewrite Cuppa3 AST into a form that is
# easily used to generate code for exp2bytecode.

# Just as in previous compilers we do not use the symbol symbol_table
# table to hold values but to hold (name, target_name) pairs.

from cuppa3_cc_state import state
from grammar_stuff import assert_match

#########################################################################
temp_cnt = 0

def make_temp_name():
    global temp_cnt
    new_name = "v$" + str(temp_cnt)
    temp_cnt += 1
    return new_name

#########################################################################
def declare_temp():
    name = make_temp_name()
    state.symbol_table.declare_scalar(name)
    target_name = state.symbol_table.get_target_name(name)
    return target_name

#########################################################################
def len_seq(seq_list):
    # seq_list can either be a ('seq', item, rest) node or a ('nil',) node.

    if seq_list[0] == 'nil':
        return 0

    elif seq_list[0] == 'seq':
        # unpack the seq node
        (SEQ, p1, p2) = seq_list

        return 1 + len_seq(p2)

    else:
            raise ValueError("unknown node type: {}".format(seq_list[0]))

#########################################################################
def eval_actual_args(args):
    # args can either be a ('seq', item, rest) node or a ('nil',) node.

    if args[0] == 'nil':
        return ('nil',)

    elif args[0] == 'seq':
        # unpack the seq node
        (SEQ, arg, rest) = args

        t = walk(arg)

        return ('seq', t, eval_actual_args(rest))

    else:
        raise ValueError("unknown node type: {}".format(args[0]))

#########################################################################
def declare_formal_args(formal_args):
    # formal_args can either be a ('seq', item, rest) node or a ('nil',) node.

    if formal_args[0] == 'nil':
        return ('nil',)

    else:
        # unpack the args
        (SEQ, (ID, sym), rest) = formal_args

        # declare the variable
        state.symbol_table.declare_scalar(sym)
        target_name = state.symbol_table.get_target_name(sym)

        return ('seq', target_name, declare_formal_args(rest))

#########################################################################
def handle_call(call_kind, name, actual_arglist):

    (type, val) = state.symbol_table.lookup_sym(name)

    if type != 'function':
        raise ValueError("{} is not a function".format(name))

    # unpack the funval tuple
    (FUNVAL, formal_arglist) = val

    if len_seq(formal_arglist) != len_seq(actual_arglist):
        raise ValueError("function {} expects {} arguments" \
                         .format(sym, len_seq(formal_arglist)))

    # convert the actual values into three-address codes
    actual_val_args = eval_actual_args(actual_arglist)

    if call_kind == 'callexp':
        return ('callexp', declare_temp(), name, actual_val_args)
    else:
        return ('callstmt', name, actual_val_args)

#########################################################################
# node functions
#########################################################################
def seq(node):

    (SEQ, stmt, stmt_list) = node
    assert_match(SEQ, 'seq')

    t1 = walk(stmt)
    t2 = walk(stmt_list)

    return ('seq', t1, t2)

#########################################################################
def nil(node):

    (NIL,) = node
    assert_match(NIL, 'nil')

    return ('nil',)

#########################################################################
# Note: We are walking the body of a function declaration to figure out
# how many local variables there are. We need this information in order
# to compute the frame size of the function. Also, we need to replace
# original function local variables with their stack frame target names.
def fundecl_stmt(node):

    try: # try the fundecl pattern without arglist
        (FUNDECL, name, (NIL,), body) = node
        assert_match(FUNDECL, 'fundecl')
        assert_match(NIL, 'nil')

    except ValueError: # try fundecl with arglist
        (FUNDECL, name, arglist, body) = node
        assert_match(FUNDECL, 'fundecl')

        # we don't need the function body - abbreviated function value
        funval = ('funval', arglist)
        state.symbol_table.declare_fun(name, funval)

        state.symbol_table.enter_function()
        new_arglist = declare_formal_args(arglist)
        t = walk(body)
        state.symbol_table.exit_function()
        frame_size = state.symbol_table.get_frame_size()

        return ('fundef', name, new_arglist, t, frame_size)


    else: # fundecl pattern matched
        # no arglist is present
        # we don't need the function body - abbreviated function value
        funval = ('funval', ('nil',))
        state.symbol_table.declare_fun(name, funval)

        state.symbol_table.enter_function()
        t = walk(body)
        state.symbol_table.exit_function()
        frame_size = state.symbol_table.get_frame_size()

        return ('fundef', name, ('nil',), t, frame_size)

#########################################################################
def declare_stmt(node):

    try: # try the declare pattern without initializer
        (DECLARE, name, (NIL,)) = node
        assert_match(DECLARE, 'declare')
        assert_match(NIL, 'nil')

    except ValueError: # try declare with initializer
        (DECLARE, name, init_val) = node
        assert_match(DECLARE, 'declare')

        t = walk(init_val)
        state.symbol_table.declare_scalar(name)
        target_name = state.symbol_table.get_target_name(name)

        return ('assign', target_name, t)

    else: # declare pattern matched
        # when no initializer is present we init with the value 0
        state.symbol_table.declare_scalar(name)
        target_name = state.symbol_table.get_target_name(name)

        return ('assign', target_name, ('integer', 0))

#########################################################################
def assign_stmt(node):

    (ASSIGN, name, exp) = node
    assert_match(ASSIGN, 'assign')

    t = walk(exp)
    target_name = state.symbol_table.get_target_name(name)

    return ('assign', target_name, t)

#########################################################################
def get_stmt(node):

    (GET, name) = node
    assert_match(GET, 'get')

    target_name = state.symbol_table.get_target_name(name)

    return ('get', target_name)

#########################################################################
def put_stmt(node):

    (PUT, exp) = node
    assert_match(PUT, 'put')

    t = walk(exp)

    return ('put', t)

#########################################################################
def call_stmt(node):

    (CALLSTMT, name, actual_args) = node
    assert_match(CALLSTMT, 'callstmt')

    return handle_call('callstmt', name, actual_args)

#########################################################################
def return_stmt(node):

    try: # try return without exp
        (RETURN, (NIL,)) = node
        assert_match(RETURN, 'return')
        assert_match(NIL, 'nil')

        if not state.symbol_table.in_function:
            raise ValueError("return has to appear in a function context.")

        return ('return', ('nil',))

    except ValueError: # return with exp
        (RETURN, exp) = node
        assert_match(RETURN, 'return')

        if not state.symbol_table.in_function:
            raise ValueError("return has to appear in a function context.")

        t = walk(exp)

        return ('return', t)

#########################################################################
def while_stmt(node):

    (WHILE, cond, body) = node
    assert_match(WHILE, 'while')

    t1 = walk(cond)
    t2 = walk(body)

    return ('while', t1, t2)

#########################################################################
def if_stmt(node):

    try: # try the if-then pattern
        (IF, cond, then_stmt, (NIL,)) = node
        assert_match(IF, 'if')
        assert_match(NIL, 'nil')

    except ValueError: # if-then pattern didn't match
        (IF, cond, then_stmt, else_stmt) = node
        assert_match(IF, 'if')

        t1 = walk(cond)
        t2 = walk(then_stmt)
        t3 = walk(else_stmt)

        return ('if', t1, t2, t3)

    else: # if-then pattern matched
        t1 = walk(cond)
        t2 = walk(then_stmt)

        return ('if', t1, t2, ('nil',))

#########################################################################
def block_stmt(node):

    (BLOCK, stmt_list) = node
    assert_match(BLOCK, 'block')

    state.symbol_table.push_scope()
    t = walk(stmt_list)
    state.symbol_table.pop_scope()

    return ('block', t)

#########################################################################
def binop_exp(node):
    # turn expressions into three-address codes

    (OP, c1, c2) = node
    if OP not in ['+', '-', '*', '/', '==', '<=']:
        raise ValueError("pattern match failed on " + OP)

    t1 = walk(c1)
    t2 = walk(c2)

    target_name = declare_temp()

    return (OP, target_name, t1, t2)

#########################################################################
def integer_exp(node):

    (INTEGER, value) = node
    assert_match(INTEGER, 'integer')

    return ('integer', value)

#########################################################################
def id_exp(node):

    (ID, name) = node
    assert_match(ID, 'id')

    target_name = state.symbol_table.get_target_name(name)

    return ('id', target_name)

#########################################################################
def call_exp(node):

    (CALLEXP, name, actual_args) = node
    assert_match(CALLEXP, 'callexp')

    return handle_call('callexp', name, actual_args)

#########################################################################
def uminus_exp(node):

    (UMINUS, exp) = node
    assert_match(UMINUS, 'uminus')

    t = walk(exp)

    target_name = declare_temp()

    return ('uminus', target_name, t)

#########################################################################
def not_exp(node):

    (NOT, exp) = node
    assert_match(NOT, 'not')

    t = walk(exp)

    target_name = declare_temp()

    return ('not', target_name, t)

#########################################################################
def paren_exp(node):

    (PAREN, exp) = node
    assert_match(PAREN, 'paren')

    # get rid of parenthesis - not necessary in AST
    return walk(exp)

#########################################################################
# walk
#########################################################################
def walk(node):
    # node format: (TYPE, [child1[, child2[, ...]]])
    type = node[0]

    if type in dispatch_dict:
        node_function = dispatch_dict[type]
        return node_function(node)
    else:
        raise ValueError("walk: unknown tree node type: " + type)

# a dictionary to associate tree nodes with node functions
dispatch_dict = {
    'seq'     : seq,
    'nil'     : nil,
    'fundecl' : fundecl_stmt,
    'declare' : declare_stmt,
    'assign'  : assign_stmt,
    'get'     : get_stmt,
    'put'     : put_stmt,
    'callstmt': call_stmt,
    'return'  : return_stmt,
    'while'   : while_stmt,
    'if'      : if_stmt,
    'block'   : block_stmt,
    'integer' : integer_exp,
    'id'      : id_exp,
    'callexp' : call_exp,
    'paren'   : paren_exp,
    '+'       : binop_exp,
    '-'       : binop_exp,
    '*'       : binop_exp,
    '/'       : binop_exp,
    '=='      : binop_exp,
    '<='      : binop_exp,
    'uminus'  : uminus_exp,
    'not'     : not_exp
}
