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
    # symbol declaration functions - the basic idea is that a
    # declaration creates a property tuple associated with a symbol.
    # that property tuple holds such things as the type of symbol,
    # the data type of the symbol and its value.

    def declare_scalar(self, sym, data_type, value):
        '''
        declare a scalar symbol in the current scope.
        '''
        # first we need to check whether the symbol was already declared
        # at this scope
        if sym in self.scoped_symtab[CURR_SCOPE]:
            raise ValueError("symbol {} already declared".format(sym))

        # enter the symbol with its property tuple in the current scope
        property_tuple = ('scalar', data_type, value)
        self.scoped_symtab[CURR_SCOPE].update({sym : property_tuple})

    def declare_function(self, sym, return_data_type, funval):
        '''
        declare a function symbol in the current scope.
        '''
        # first we need to check whether the symbol was already declared
        # at this scope
        if sym in self.scoped_symtab[CURR_SCOPE]:
            raise ValueError("symbol {} already declared".format(sym))

        # enter the symbol with its property tuple in the current scope
        property_tuple = ('function', return_data_type, funval)
        self.scoped_symtab[CURR_SCOPE].update({sym : property_tuple})

    #####################################################################
    # Misc. functions

    def lookup_sym(self, sym):
        '''
        find the first occurence of sym in the symtab stack
        and return the associated property tuple
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
