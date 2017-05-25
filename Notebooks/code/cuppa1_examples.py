fact = \
'''
get x;
y = 1;
while (1 <= x)
{
      y = y * x;
      x = x - 1;
}
put y;
'''

list = \
'''
// list of integers
get x
while (1 <= x) 
{
    put x;
    x = x + - 1;
    i = x
}
'''

ifex = \
'''
// logical not in Cuppa1
get x
if (x == 0)
   put 1
else 
  put 0
'''

logical_and = \
'''
// logical and in Cuppa1 can be simulated with multiplication
x = 0
y = 0
put x
put y
put x * y

x = 1
y = 0
put x
put y
put x * y

x = 0
y = 1
put x
put y
put x * y

x = 1
y = 1
put x
put y
put x * y
'''

logical_or = \
'''
// logical or in Cuppa1 can be simulated with addition
x = 0
y = 0
put x
put y
put x + y

x = 1
y = 0
put x
put y
put x + y

x = 0
y = 1
put x
put y
put x + y

x = 1
y = 1
put x
put y
put not not (x + y) // make it look like '1'
'''

