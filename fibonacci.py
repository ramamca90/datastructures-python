#0, 1, 1, 2, 3, 5, 8, 11, 19, 30

#recursion - find nth fibonacci(Here not storing intermediate results, so unnecessary recursive calls)
def nth_fibonacci(n):
    if n == 1:
        return 0
    
    if n == 2:
        return 1
      
    return nth_fibonacci(n-1) + nth_fibonacci(n-2)

n = 37

assert isinstance(n, int) and n > 0, "Number should be positive no"
nth_fibonacci(n)

#Recursion(memoization ) - find nth fibonacci - storing intermediate results
fib = {
    1: 0,
    2: 1
}

def nth_fibonacci(n):
    if n in fib:
        return fib[n]
    
    result = nth_fibonacci(n-1) + nth_fibonacci(n-2)
    fib[n] = result
    return result

n = 60

assert isinstance(n, int) and n > 0, "Number should be positive no"

print(nth_fibonacci(n))

#Iteration(Using Generator) - get first n nos
def find_n_fibonaccis(n):
    n1 = 0
    n2 = 1
    
    n3 = n1
    
    while n:
        yield n3
        n1, n2 = n2, n3
        n3 = n1 + n2
        n -= 1

num = 10
if not isinstance(num, int) or num <= 0:
    print("Number should be positive no")
else:   
    for i in find_n_fibonaccis(num):
        print(i, end=" ")
        
#Iteration - get first n nos
def find_n_fibonaccis(n):
    n1 = 0
    n2 = 1
    
    n3 = n1
    
    while n:
        print(n3)
        n1, n2 = n2, n3
        n3 = n1 + n2
        n -= 1

num = 10
if not isinstance(num, int) or num <= 0:
    print("Number should be positive no")
else:   
    find_nth_fibonacci(num)
    
