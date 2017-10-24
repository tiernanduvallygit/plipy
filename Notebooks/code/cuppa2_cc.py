#!/usr/bin/env python
# Cuppa2 compiler

from argparse import ArgumentParser
from cuppa2_lex import lexer
from cuppa2_cc_frontend_gram import parser
from cuppa2_cc_state import state
from cuppa2_cc_codegen import walk as codegen
from cuppa2_cc_output import output

def cc(input_stream):

    # initialize the state object
    state.initialize()

    # build the AST
    parser.parse(input_stream, lexer=lexer)

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
