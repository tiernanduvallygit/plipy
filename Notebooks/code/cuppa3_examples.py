add = \
'''
declare add(a,b) 
{
    return a+b;
}

declare x = add(3,2);
put x;
'''

seqsum = \
'''
declare seqsum(n) 
{
    
    declare add(a,b) return a+b;
    declare inc(x) return x+1;
        
    declare i = 1;
    declare sum = 0;
        
    while (i <= n) 
    {
        sum = add(sum,i);
        i = inc(i);
    }
        
    return sum;
}

put seqsum(10);
'''

and_prog = \
'''
declare and(a,b)
{
    return a*b;
}


declare v;
declare w;
get v;
get w;

// enter v = -1 to stop loop
while (0 <= v) 
{
    put and(v,w)
    get v;
    get w;
}
'''

fact = \
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

factrec = \
'''
// recursive implementation of factorial
declare fact(x) 
{
     if (x <= 1)
        return 1;
     else 
        return x * fact(x-1);
}

// ask the user for input
declare v;
get v;
put fact(v);
'''

fold = \
'''
declare x = (3 + 2) / 5;
put x;
'''


func1 = \
'''
declare f () {
 put(1001);
}

f();
'''

