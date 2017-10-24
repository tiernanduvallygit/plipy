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
    
    declare add(a,b) 
    {
        return a+b;
    }
        
    declare i = 1;
    declare sum = 0;
        
    while (i <= n) 
    {
        sum = add(sum,i);
        i = i + 1;
    }
        
    put sum;
}

seqsum(10);
'''

and_prog = \
'''
declare and(a,b) {
    if (a)
        if(b)
            return 1;
   return 0;
}


declare v;
declare w;
get v;
get w;

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
     declare y;
     if (x <= 1)
        return 1;
     else 
     {
        y = x*fact(x-1);
        return y;
      }
}

declare v;
get v;
put fact(v);
'''

fibonacci = \
'''
declare F(n)
{
   if (n==0)
      return 0;
   else if (n==1)
      return 1;
   else
      return F(n-1)+F(n-2);
}

declare v;
get v;
while (0 <= v) 
{
   put F(v);
   get v;
}
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

