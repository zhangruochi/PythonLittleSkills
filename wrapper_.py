#修饰器trace的作用   fibonacci = trace(fibonacci)

def trace(func):
    
    def wapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("{0}({1}, {2}) -> {3}".format(func.__name__,args,kwargs,result))
        return result
    return wapper

@trace
def fibonacci(n):
    """Return the n-th Fibonacci number""" 
    return n if n in (0,1) else fibonacci(n-1) + fibonacci(n-2)


#-------使用 functools.wraps----------
from functools import wraps
def trace2(func):
    @wraps(func)
    def wapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("{0}({1}, {2}) -> {3}".format(func.__name__,args,kwargs,result))
        return result
    return wapper

@trace2
def fibonacci2(n):
    """Return the n-th Fibonacci number.""" 
    return n if n in (0,1) else fibonacci(n-1) + fibonacci(n-2)



if __name__ == '__main__':
    fibonacci(3)
    print(fibonacci) #<function trace.<locals>.wapper at 0x1006e9d08>
    help(fibonacci)
    print('--------------------------')
    fibonacci2(3)
    print(fibonacci2) #<function fibonacci2 at 0x1020de2f0>
    help(fibonacci2)


            

