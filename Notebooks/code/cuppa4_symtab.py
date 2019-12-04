#########################################################################
# symbol table for Cuppa4
#
# it is a scoped symbol table with a dictionary at each scope level
#
#########################################################################

CURR_SCOPE = 0

class SymTab:

    def __init__(self):
        '''
        constructor: define and initialize all data structures
        '''
        # global scope dictionary must always be present
        self.scoped_symtab = [{}]

    #####################################################################
    # scope manipulation functions

    def get_config(self):
        '''
        current configuration is a shallow copy of the dictionary stack
        '''
        return list(self.scoped_symtab)

    def set_config(self, c):
        '''
        replace the configuration of the symbol table with another
        '''
        self.scoped_symtab = c

    def push_scope(self):
        '''
        push a new dictionary onto the stack - stack grows to the left
        '''
        self.scoped_symtab.insert(CURR_SCOPE,{})

    def pop_scope(self):
        '''
        pop the current (left most) dictionary off the stack
        '''
        if len(self.scoped_symtab) == 1:
            raise ValueError("cannot pop the global scope")
        else:
            self.scoped_symtab.pop(CURR_SCOPE)

    #####################################################################
    # symbol functions
    # types of symbol values:
    #     ('scalar-val', type, val)
    #     ('function-val', return_data_type, arglist, body, context)

    def declare_scalar(self, sym, data_type, init_val):
        '''
        declare a symbol in the current scope.
        '''
        # first we need to check whether the symbol was already declared
        # at this scope
        if sym in self.scoped_symtab[CURR_SCOPE]:
            raise ValueError("symbol {} already declared".format(sym))

        # enter the symbol with its value in the current scope
        value = ('scalar-val', data_type, init_val)
        self.scoped_symtab[CURR_SCOPE].update({sym : value})

    def declare_fun(self, sym, return_data_type, arglist, body, context):
        '''
        declare a symbol in the current scope.
        '''
        # first we need to check whether the symbol was already declared
        # at this scope
        if sym in self.scoped_symtab[CURR_SCOPE]:
            raise ValueError("symbol {} already declared".format(sym))

        # enter the symbol with its value in the current scope
        value = ('function-val', return_data_type, ('lambda', arglist, body, context))
        self.scoped_symtab[CURR_SCOPE].update({sym : value})

    def lookup_sym(self, sym):
        '''
        find the first occurence of sym in the symtab stack
        and return the associated value
        '''
        n_scopes = len(self.scoped_symtab)

        for scope in range(n_scopes):
            if sym in self.scoped_symtab[scope]:
                return self.scoped_symtab[scope].get(sym)

        # not found
        raise ValueError("{} was not declared".format(sym))

    def update_sym(self, sym, val):
        '''
        find the first occurence of sym in the symtab stack
        and update the associated value
        '''
        n_scopes = len(self.scoped_symtab)

        for scope in range(n_scopes):
            if sym in self.scoped_symtab[scope]:
                self.scoped_symtab[scope].update({sym : val})
                return

        # not found
        raise ValueError("{} was not declared".format(sym))

#########################################################################
