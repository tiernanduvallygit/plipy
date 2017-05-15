from exp1_pp_gram import parser

def exp1_pp(input_stream = None):
    'A driver for our Exp1 pretty printer.'
    
    if not input_stream:
        input_stream = input("exp1 > ")
    
    parser.parse(input_stream)

