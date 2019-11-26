#!/usr/bin/env python
# Cuppa3 compiler

from argparse import ArgumentParser
from cuppa3_lex import lexer
from cuppa3_cc_frontend import parser
from cuppa3_cc_state import state
from cuppa3_cc_tree_rewrite import walk as rewrite
from cuppa3_cc_codegen import walk as codegen
from cuppa3_cc_output import output

def cc(input_stream):

    # initialize the state object
    state.initialize()

    # build the AST
    parser.parse(input_stream, lexer=lexer)

    # rewrite the AST - lower the abstraction level
    state.AST = rewrite(state.AST)

    # generate the list of instruction tuples
    instr_stream = codegen(state.AST) + [('stop',)]

    # output the instruction stream
    bytecode = output(instr_stream)

    return bytecode

if __name__ == "__main__":
    # parse command line args
    aparser = ArgumentParser()
    aparser.add_argument('input', metavar='input_file', help='cuppa1 input file')
    aparser.add_argument('-o', metavar='output_file', help='exp1bytecode output file')

    args = vars(aparser.parse_args())

    f = open(args['input'], 'r')
    input_stream = f.read()
    f.close()

    # run the compiler
    bytecode = cc(input_stream=input_stream)

    if not args['o']:
        print(bytecode)

    else:
        f = open(args['o'], 'w')
        f.write(bytecode)
        f.close()
