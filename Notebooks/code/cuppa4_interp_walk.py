# A tree walker to interpret Cuppa4 programs

from cuppa4_state import state
from grammar_stuff import assert_match

#########################################################################
# Use the exception mechanism to return values from function calls

class ReturnValue(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return(repr(self.value))

#########################################################################
# type promotion tables for builtin primitive types.  these tables
# implement the type hierarchy
#
#             integer < float < string
#             void

_promote_table = {
  'string' : {'string': 'string', 'float': 'string', 'integer': 'string',  'void': 'void'},
  'float'  : {'string': 'string', 'float': 'float',  'integer': 'float',   'void': 'void'},
  'integer': {'string': 'string', 'float': 'float',  'integer': 'integer', 'void': 'void'},
  'void'   : {'string': 'void',   'float': 'void',   'integer': 'void',    'void': 'void'},
}

_conversion_table = {
  'string' : {'string': str,  'float': str,   'integer': str,   'void': None},
  'float'  : {'string': str,  'float': float, 'integer': float, 'void': None},
  'integer': {'string': str,  'float': float, 'integer': int,   'void': None},
  'void'   : {'string': None, 'float': None,  'integer': None,  'void': None},
}

_safe_assign_table = {
  'string' : {'string': True,  'float': True,  'integer': True,  'void': False},
  'float'  : {'string': False, 'float': True,  'integer': True,  'void': False},
  'integer': {'string': False, 'float': False, 'integer': True,  'void': False},
  'void'   : {'string': False, 'float': False, 'integer': False, 'void': False},
}

def promote(type1, type2):
    return _promote_table.get(type1).get(type2)

def conversion_fun(ltype, rtype):
    return _conversion_table.get(ltype).get(rtype)

def safe_assign(ltype, rtype):
        return _safe_assign_table.get(ltype).get(rtype)

#########################################################################
def len_seq(seq_list):

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

    if args[0] == 'nil':
        return ('nil',)

    elif args[0] == 'seq':
        # unpack the seq node
        (SEQ, p1, p2) = args

        (data_type, val) = walk(p1)

        return ('seq', (data_type, val), eval_actual_args(p2))

    else:
        raise ValueError("unknown node type: {}".format(args[0]))

#########################################################################
def declare_formal_args(formal_args, actual_val_args):

    if len_seq(actual_val_args) != len_seq(formal_args):
        raise ValueError("actual and formal argument lists do not match")

    if formal_args[0] == 'nil':
        return

    # unpack the args
    (SEQ, (FORMALARG, formal_type, formal_arg), p1) = formal_args
    (SEQ, (actual_type, actual_arg), p2) = actual_val_args

    # declare the variable
    if not safe_assign(formal_type, actual_type):
        raise ValueError("cannot assign a value of type {} to formal argument {} of type {}"\
                         .format(actual_type, formal_arg, formal_type))

    value = conversion_fun(formal_type, actual_type)(actual_arg)
    state.symbol_table.declare_scalar(formal_arg, formal_type, value)

    declare_formal_args(p1, p2)

#########################################################################
def handle_call(name, actual_arglist):

    val = state.symbol_table.lookup_sym(name)

    if val[0] != 'function-val':
        raise ValueError("{} is not a function".format(name))

    # unpack the funval tuple
    (FUNVAL, return_data_type, lambda_val) = val
    (LAMBDA, formal_arglist, body, context) = lambda_val

    if len_seq(formal_arglist) != len_seq(actual_arglist):
        raise ValueError("function {} expects {} arguments"\
                         .format(name, len_seq(formal_arglist)))

    # set up the environment for static scoping and then execute the function
    actual_val_args = eval_actual_args(actual_arglist)   # evaluate actuals in current symtab
    save_symtab = state.symbol_table.get_config()        # save current symtab

    state.symbol_table.set_config(context)               # make function context current symtab
    state.symbol_table.push_scope()                      # push new function scope
    declare_formal_args(formal_arglist, actual_val_args) # declare formals in function scope

    return_value = None
    try:
        walk(body)                                       # execute the function
    except ReturnValue as val:
        if return_data_type == 'void' and not val.value is None:
            raise ValueError("the void function {} cannot return a value".format(name))
        elif return_data_type == 'void' and val.value is None:
            return_value = None
        elif return_data_type != 'void' and val.value is None:
            raise ValueError("the function {} of type {} return no value".format(name, return_data_type))
        else:
            # make sure that we are returning the correct type
            (data_type, _) = val.value
            if not safe_assign(return_data_type, data_type):
                raise ValueError("return statement in {} returned a value of type {} instead of the expected {}".format(name, data_type, return_data_type))
            return_value = val.value

    # NOTE: popping the function scope is not necessary because we
    # are restoring the original symtab configuration
    state.symbol_table.set_config(save_symtab)           # restore original symtab config

    return return_value

#########################################################################
# node functions
#########################################################################
def seq(node):

    (SEQ, stmt, stmt_list) = node
    assert_match(SEQ, 'seq')

    walk(stmt)
    walk(stmt_list)

#########################################################################
def nil(node):

    (NIL,) = node
    assert_match(NIL, 'nil')

    # do nothing!
    pass

#########################################################################
def fundecl_stmt(node):

    (FUNDECL, return_data_type, name, arglist, body) = node
    assert_match(FUNDECL, 'fundecl')

    context = state.symbol_table.get_config()
    state.symbol_table.declare_fun(name, return_data_type, arglist, body, context)

#########################################################################
def scalardecl_stmt(node):

    try: # try the declare pattern without initializer
        (SCALARDECL, data_type, name, (NIL,)) = node
        assert_match(SCALARDECL, 'scalardecl')
        assert_match(NIL, 'nil')

    except ValueError: # try declare with initializer
        (SCALARDECL, data_type, name, init_val) = node
        assert_match(SCALARDECL, 'scalardecl')

        (t, v) = walk(init_val)

        if not safe_assign(data_type, t):
            raise ValueError(\
              "a value of type {} cannot be assigned to the variable {} of type {}"\
              .format(t,name,data_type))

        state.symbol_table \
             .declare_scalar(name, data_type, conversion_fun(data_type,t)(v))

    else: # declare pattern matched
        # when no initializer is present we init with the value 0
        state.symbol_table \
             .declare_scalar(name, data_type, conversion_fun(data_type,'integer')(0))

#########################################################################
def assign_stmt(node):

    (ASSIGN, name, exp) = node
    assert_match(ASSIGN, 'assign')

    (sym_type, data_type, *_) = state.symbol_table.lookup_sym(name)

    if sym_type != 'scalar-val':
        raise ValueError("Cannot assign a value to the name {}"\
                         .format(name))

    (t, v) = walk(exp)

    if not safe_assign(data_type, t):
        raise ValueError(\
          "a value of type {} cannot be assigned to the variable {} of type {}"\
          .format(t,name,data_type))

    value = (sym_type, data_type, conversion_fun(data_type,t)(v))
    state.symbol_table.update_sym(name, value)

#########################################################################
def get_stmt(node):

    (GET, name) = node
    assert_match(GET, 'get')

    (sym_type, data_type, *_) = state.symbol_table.lookup_sym(name)

    if sym_type != 'scalar-val':
        raise ValueError(\
            "Cannot assign a value to the name {} in a get"\
            .format(name))

    s = input("Value for " + name + '? ')

    try:
        if data_type == 'integer':
            value = ('scalar-val', 'integer', int(s))
        elif data_type == 'float':
            value = ('scalar-val', 'float', float(s))
        elif data_type == 'string':
            value = ('scalar-val', 'string', s)
    except ValueError:
        raise ValueError(\
            "unexpected value for variable {} of type {}"\
            .format(name, data_type))
    else:
        raise ValueError(\
            "variable {} of type {} and not supported in get statement"\
            .format(name, data_type))

    state.symbol_table.update_sym(name, sym_type, value)

#########################################################################
def put_stmt(node):

    (PUT, exp) = node
    assert_match(PUT, 'put')

    (t, v) = walk(exp)
    print("{}".format(v))

#########################################################################
def call_stmt(node):

    (CALLSTMT, name, actual_args) = node
    assert_match(CALLSTMT, 'callstmt')

    handle_call(name, actual_args)

#########################################################################
def return_stmt(node):
    # if a return value exists the return stmt will record it
    # in the state object

    try: # try return without exp
        (RETURN, (NIL,)) = node
        assert_match(RETURN, 'return')
        assert_match(NIL, 'nil')

    except ValueError: # return with exp
        (RETURN, exp) = node
        assert_match(RETURN, 'return')

        value = walk(exp)
        raise ReturnValue(value)

    else: # return without exp
        raise ReturnValue(None)

#########################################################################
def while_stmt(node):

    (WHILE, cond, body) = node
    assert_match(WHILE, 'while')

    (t, v) = walk(cond)

    if t != 'integer':
        raise ValueError("the while condition has to be an integer expression")

    while v != 0:
        walk(body)
        (_, v) = walk(cond)

#########################################################################
def if_stmt(node):

    try: # try the if-then pattern
        (IF, cond, then_stmt, (NIL,)) = node
        assert_match(IF, 'if')
        assert_match(NIL, 'nil')

    except ValueError: # if-then pattern didn't match
        (IF, cond, then_stmt, else_stmt) = node
        assert_match(IF, 'if')

        (t, v) = walk(cond)

        if t != 'integer':
            raise ValueError("the if condition has to be an integer expression")

        if v != 0:
            walk(then_stmt)
        else:
            walk(else_stmt)

    else: # if-then pattern matched
        (t, v) = walk(cond)

        if t != 'integer':
            raise ValueError("the if condition has to be an integer expression")

        if v != 0:
            walk(then_stmt)

#########################################################################
def block_stmt(node):

    (BLOCK, stmt_list) = node
    assert_match(BLOCK, 'block')

    state.symbol_table.push_scope()
    walk(stmt_list)
    state.symbol_table.pop_scope()

#########################################################################
def plus_exp(node):

    (PLUS,c1,c2) = node
    assert_match(PLUS, '+')

    (t1, v1) = walk(c1)
    (t2, v2) = walk(c2)

    type = promote(t1, t2)

    if type in ['integer', 'float']:
        return (type, v1 + v2)
    elif type == 'string':
        return ('string', str(v1) + str(v2))
    else:
        raise ValueError('unsupported type {} in + operator'.format(type))

#########################################################################
def minus_exp(node):

    (MINUS,c1,c2) = node
    assert_match(MINUS, '-')

    (t1, v1) = walk(c1)
    (t2, v2) = walk(c2)

    type = promote(t1, t2)

    if type in ['integer', 'float']:
         return (type, v1 - v2)
    else:
        raise ValueError('unsupported type {} in - oerator'.format(type))

#########################################################################
def times_exp(node):

    (TIMES,c1,c2) = node
    assert_match(TIMES, '*')

    (t1, v1) = walk(c1)
    (t2, v2) = walk(c2)

    type = promote(t1, t2)

    if type in ['integer', 'float']:
         return (type, v1 * v2)
    else:
        raise ValueError('unsupported type {} in * oerator'.format(type))

#########################################################################
def divide_exp(node):

    (DIVIDE,c1,c2) = node
    assert_match(DIVIDE, '/')

    (t1, v1) = walk(c1)
    (t2, v2) = walk(c2)

    type = promote(t1, t2)

    if type in ['integer', 'float']:
         return ('float', v1 / v2) # in Python division always returns a float
    else:
        raise ValueError('unsupported type {} in / oerator'.format(type))

#########################################################################
def eq_exp(node):

    (EQ,c1,c2) = node
    assert_match(EQ, '==')

    (_, v1) = walk(c1)
    (_, v2) = walk(c2)

    # we reuse Python's semantics
    return ('integer', 1 if v1 == v2 else 0)

#########################################################################
def le_exp(node):

    (LE,c1,c2) = node
    assert_match(LE, '<=')

    (_, v1) = walk(c1)
    (_, v2) = walk(c2)

    # we reuse Python's semantics
    return ('integer', 1 if v1 <= v2 else 0)

#########################################################################
def id_exp(node):

    (ID, name) = node
    assert_match(ID, 'id')

    val = state.symbol_table.lookup_sym(name)

    if val[0] != 'scalar-val':
        raise ValueError("{} is not a scalar in expression".format(name))

    (SCALAR_VAL, data_type, v) = val

    return (data_type, v)

#########################################################################
def call_exp(node):
    # call_exp works just like call_stmt with the exception
    # that we have to pass back a return value

    (CALLEXP, name, args) = node
    assert_match(CALLEXP, 'callexp')

    return_value = handle_call(name, args)

    if return_value is None:
        raise ValueError("No return value from function {}".format(name))

    return return_value

#########################################################################
def uminus_exp(node):

    (UMINUS, exp) = node
    assert_match(UMINUS, 'uminus')

    (t, v) = walk(exp)

    if t in ['integer', 'float']:
        return (t, - v)
    else:
        raise ValueError("unsupported type {} in unary minus expression".format(t))

#########################################################################
def not_exp(node):

    (NOT, exp) = node
    assert_match(NOT, 'not')

    (t, v) = walk(exp)

    if t == 'integer':
        return ('integer', 0 if v != 0 else 1)
    else:
        raise ValueError("unsupported type {} in not expression".format(t))

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
    'seq'        : seq,
    'nil'        : nil,
    'fundecl'    : fundecl_stmt,
    'scalardecl' : scalardecl_stmt,
    'assign'     : assign_stmt,
    'get'        : get_stmt,
    'put'        : put_stmt,
    'callstmt'   : call_stmt,
    'return'     : return_stmt,
    'while'      : while_stmt,
    'if'         : if_stmt,
    'block'      : block_stmt,
    'integer'    : lambda node: node,
    'float'      : lambda node: node,
    'string'     : lambda node: node,
    'id'         : id_exp,
    'callexp'    : call_exp,
    '+'          : plus_exp,
    '-'          : minus_exp,
    '*'          : times_exp,
    '/'          : divide_exp,
    '=='         : eq_exp,
    '<='         : le_exp,
    'uminus'     : uminus_exp,
    'not'        : not_exp
}
