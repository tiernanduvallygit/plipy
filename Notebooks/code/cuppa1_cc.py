#!/usr/bin/env python
# Cuppa1 compiler

from sys import stdin
from cuppa1_frontend_gram import parser
from cuppa1_state import state
from cuppa1_codegen_walk import walk as codegen

def cc(input_stream = None):

    # if no input stream was given read from stdin
    if not input_stream:
        input_stream = stdin.read()

    # initialize the state object
    state.initialize()

    # build the AST
    parser.parse(input_stream)

    # walk the AST
    code = codegen(state.AST)

    # output the pretty printed code
    print(code)

if __name__ == "__main__":
    # execute only if run as a script
    cc()