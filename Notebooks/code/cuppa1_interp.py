#!/usr/bin/env python
# Cuppa1 interpreter

from sys import stdin
from cuppa1_frontend_gram import parser
from cuppa1_state import state
from cuppa1_interp_walk import walk

def interp(input_stream = None):

    # if no input stream was given read from stdin
    if not input_stream:
        input_stream = stdin.read()

    # initialize the state object
    state.initialize()

    # build the AST
    parser.parse(input_stream)

    # walk the AST
    walk(state.AST)

if __name__ == "__main__":
    # execute only if run as a script
    interp()