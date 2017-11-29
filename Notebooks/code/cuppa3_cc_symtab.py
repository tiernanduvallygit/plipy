#########################################################################
# symbol table for Cuppa3
#
# it is a scoped symbol table with a dictionary at each scope level
#
#########################################################################

CURR_SCOPE = 0

class SymTab:

    #-------
    def __init__(self):
        # global scope dictionary must always be present
        self.scoped_symtab = [{}]
        # keep track of wether we are in a function declaration of not
        self.in_function = False
        # counter used to generate unique global names
        self.temp_cnt = 0
        # counter to compute the frameoffset of function local variables
        self.offset_cnt = 0

    #-------
    def make_target_name(self):
        # in functions all function local variables are on the runtime stack
        if self.in_function:
            name = "%tsx[0]" if self.offset_cnt == 0 else "%tsx[" + str(- self.offset_cnt) + "]"
            self.offset_cnt += 1
        else:
            name = "t$" + str(self.temp_cnt)
            self.temp_cnt += 1
        return name

    #-------
    def get_frame_size(self):
        return self.offset_cnt
    
    #-------
    def get_config(self):
        # we make a shallow copy of the symbol table
        return list(self.scoped_symtab)
    
    #-------
    def set_config(self, c):
        self.scoped_symtab = c
        
    #-------
    def push_scope(self):
        # push a new dictionary onto the stack - stack grows to the left
        self.scoped_symtab.insert(CURR_SCOPE,{})

    #-------
    def pop_scope(self):
        # pop the left most dictionary off the stack
        if len(self.scoped_symtab) == 1:
            raise ValueError("cannot pop the global scope")
        else:
            self.scoped_symtab.pop(CURR_SCOPE)

    #-------
    def enter_function(self):
        # if we are in a function declaration we are not allowed to start another one
        if self.in_function:
            raise ValueError("Function declarations cannot be nested.")

        self.in_function = True
        self.push_scope()
        self.offset_cnt = 0

    #-------
    def exit_function(self):
        self.in_function = False
        self.pop_scope()

    #-------
    def declare_sym(self, sym):
        # declare the scalar in the current scope: dict @ position 0
        
        # first we need to check whether the symbol was already declared
        # at this scope
        if sym in self.scoped_symtab[CURR_SCOPE]:
            raise ValueError("symbol {} already declared".format(sym))
        
        # enter the symbol in the current scope
        scope_dict = self.scoped_symtab[CURR_SCOPE]
        scope_dict[sym] = ('scalar', self.make_target_name())

    #-------
    def declare_fun(self, sym, init):
        # declare a function in the current scope: dict @ position 0
        
        # first we need to check whether the symbol was already declared
        # at this scope
        if sym in self.scoped_symtab[CURR_SCOPE]:
            raise ValueError("symbol {} already declared".format(sym))
        
        # enter the function in the current scope
        scope_dict = self.scoped_symtab[CURR_SCOPE]
        scope_dict[sym] = ('function', init)

    #-------
    def lookup_sym(self, sym):
        # find the first occurence of sym in the symtab stack
        # and return the associated value

        n_scopes = len(self.scoped_symtab)

        for scope in range(n_scopes):
            if sym in self.scoped_symtab[scope]:
                val = self.scoped_symtab[scope].get(sym)
                return val

        # not found
        raise ValueError("{} was not declared".format(sym))

    #-------
    def get_target_name(self, sym):
        (type, name) = self.lookup_sym(sym)
        if type != 'scalar':
            raise ValueError("{} is not a scalar.".format(sym))
        return name

#########################################################################


