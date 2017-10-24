fact =\
'''
// computes the factorial of x
declare x;
declare y = 1;

get x;

while (1 <= x)
{
    y = y * x;
    x = x - 1;
}

put y;
'''

fold =\
'''
declare x = (3 + 2) / 5;
put x;
'''

if_ex =\
'''
declare y = 1

if (y == 1)
{
    put 1
}
else 
{
    put 2
}
'''

list =\
'''
// list of integers
declare x;
get x;
while (1 <= x)
{
    put x;
    x = x - 1;
}
'''

redecl =\
'''
declare x;
get x;
put x + 1;
declare x = 10;
put x;
'''

scope1 =\
'''
declare x = 1;
{
    declare x = 2;
    put x;
}
{
    declare x = 3;
    put x;
}
put x;
'''

scope2 =\
'''
declare x = 1;
put x;
{
    x = 2;
}
put x;
{
    x = 3;
}
put x;
'''

undecl =\
'''
get x;
put x + 1;
'''


