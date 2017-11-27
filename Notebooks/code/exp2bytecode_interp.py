#!/usr/bin/env python

from argparse import ArgumentParser
from exp2bytecode_lex import lexer
from exp2bytecode_interp_gram import parser
from exp2bytecode_interp_state import state
from pprint import pprint

#####################################################################################
def get_tsx():
    # compute the 'top of stack' index
    
    return len(state.runtime_stack) - 1

#####################################################################################
def do_storable(storable, val):
    # store the value in the appropriate storable
    
    tsx = get_tsx()
    
    if storable[0] == 'id':
        # ('id', name)
        name = storable[1]
        state.symbol_table[name] = val

    elif storable[0] == '%rvx':
        # ('%rvx',)
        state.rvx = val

    elif storable[0] == '%tsx':
        # ('%tsx', opt_offset_exp)
        if storable[1]:
            offset = eval_exp_tree(storable[1])
            state.runtime_stack[tsx+offset] = val
        else:
            state.runtime_stack[tsx] = val

    else:
        raise ValueError("Unknown storable {}".format(storable[0]))

#####################################################################################
def interp_program():
    'execute abstract bytecode machine'
    
    # We cannot use the list iterator here because we
    # need to be able to interpret jump instructions
    
    # start at the first instruction in program
    state.instr_ix = 0
    
    # keep interpreting until we run out of instructions
    # or we hit a 'stop'
    while True:
        if state.instr_ix == len(state.program):
            # no more instructions
            break
        else:
            # get instruction from program
            instr = state.program[state.instr_ix]
        
        # instruction format: (type, [arg1, arg2, ...])
        type = instr[0]
        
        # print("decoding instruction {}".format(type))
        
        # interpret instruction
        if type == 'print':
            # PRINT opt_string exp
            exp_tree = instr[2]
            val = eval_exp_tree(exp_tree)
            str = instr[1] if instr[1] else "> "
            print("{}{}".format(str, val))
            state.instr_ix += 1
        
        elif type == 'input':
            # INPUT opt_string storable
            storable = instr[2]
            str = instr[1] if instr[1] else "Please enter a value: "
            val = input(str)
            do_storable(storable, val)
            state.instr_ix += 1
        
        elif type == 'store':
            # STORE storable exp
            storable = instr[1] # storable itself is a tuple (type, children...)
            val = eval_exp_tree(instr[2])
            do_storable(storable, val)
            state.instr_ix += 1
        
        elif type == 'call':
            # call label
            # push the current instruction pointer
            state.runtime_stack.append(state.instr_ix)
            # get the target address from the label table
            label = instr[1]
            state.instr_ix = state.label_table.get(label, None)
            
            # print("jumping to instruction {}".format(state.instr_ix))

        elif type == 'return':
            # return
            # pop the return address off the stack and jump to it
            state.instr_ix = state.runtime_stack.pop()
            state.instr_ix += 1
            
            # print("returning to instruction {}".format(state.instr_ix))

        elif type == 'pushv':
            # pushv exp
            exp_tree = instr[1]
            val = eval_exp_tree(exp_tree)
            # push value onto stack
            state.runtime_stack.append(val)

            state.instr_ix += 1

        elif type == 'popv':
            # popv opt_storable
            storable = instr[1]
            val = state.runtime_stack.pop()

            if storable:
                do_storable(storable, val)

            state.instr_ix += 1

        elif type == 'pushf':
            # pushf size_exp
            size_val = eval_exp_tree(instr[1])
        
            # pushing a stack frame onto the stack
            # zeroing out each stack location in the frame
            for i in range(size_val):
                state.runtime_stack.append(0)

            state.instr_ix += 1

        elif type == 'popf':
            # popf size_exp
            size_val = eval_exp_tree(instr[1])
        
            # popping a stack frame off the stack
            for i in range(size_val):
                state.runtime_stack.pop()

            state.instr_ix += 1

        elif type == 'jumpT':
            # JUMPT exp label
            val = eval_exp_tree(instr[1])
            if val:
                state.instr_ix = state.label_table.get(instr[2], None)
            else:
                state.instr_ix += 1

        elif type == 'jumpF':
            # JUMPF exp label
            val = eval_exp_tree(instr[1])
            if not val:
                state.instr_ix = state.label_table.get(instr[2], None)
            else:
                state.instr_ix += 1

        elif type == 'jump':
            # JUMP label
            state.instr_ix = state.label_table.get(instr[1], None)
        
        elif type == 'stop':
            # STOP
            break

        elif type == 'noop':
            # NOOP
            state.instr_ix += 1
        
        else:
            raise ValueError("Unexpected instruction type: {}".format(p[1]))


#####################################################################################
def eval_exp_tree(node):
    'walk expression tree and evaluate to an integer value'

    # tree nodes are tuples (TYPE, [arg1, arg2,...])
    
    type = node[0]
    
    if type == '+':
        # '+' exp exp
        v_left = eval_exp_tree(node[1])
        v_right = eval_exp_tree(node[2])
        return v_left + v_right
    
    elif type == '-':
        # '-' exp exp
        v_left = eval_exp_tree(node[1])
        v_right = eval_exp_tree(node[2])
        return v_left - v_right
    
    elif type == '*':
        # '*' exp exp
        v_left = eval_exp_tree(node[1])
        v_right = eval_exp_tree(node[2])
        return v_left * v_right
    
    elif type == '/':
        # '/' exp exp
        v_left = eval_exp_tree(node[1])
        v_right = eval_exp_tree(node[2])
        return v_left // v_right
    
    elif type == '==':
        # '=' exp exp
        v_left = eval_exp_tree(node[1])
        v_right = eval_exp_tree(node[2])
        return 1 if v_left == v_right else 0
    
    elif type == '<=':
        # '<=' exp exp
        v_left = eval_exp_tree(node[1])
        v_right = eval_exp_tree(node[2])
        return 1 if v_left <= v_right else 0
    
    elif type == 'UMINUS':
        # 'UMINUS' exp
        val = eval_exp_tree(node[1])
        return - val
    
    elif type == '!':
        # '!' exp
        val = eval_exp_tree(node[1])
        return 0 if val != 0 else 1
    
    elif type == 'id':
        # 'id' var_name
        return state.symbol_table.get(node[1],0)

    elif type == '%rvx':
        # '%rvx'
        return state.rvx

    elif type == '%tsx':
        # %tsx opt_offset
        tsx = get_tsx()
        offset_exp = node[1]
        
        if offset_exp:
            val = eval_exp_tree(offset_exp)
            return state.runtime_stack[tsx+val]
        else:
            return state.runtime_stack[tsx]

    elif type == 'number':
        # NUMBER val
        return node[1]

    else:
        raise ValueError("Unexpected expression type: {}".format(type))

#####################################################################################
def interp(input_stream):
    'driver for our Exp1bytecode interpreter.'

    # initialize our abstract machine
    state.initialize()
    
    # build the IR
    parser.parse(input_stream, lexer=lexer)
    
    # pprint(state.program)
    
    # interpret the IR
    interp_program()

#####################################################################################
if __name__ == '__main__':
    # parse command line args
    aparser = ArgumentParser()
    aparser.add_argument('input')
    
    args = vars(aparser.parse_args())
    
    f = open(args['input'], 'r')
    input_stream = f.read()
    f.close()
    
    interp(input_stream=input_stream)

