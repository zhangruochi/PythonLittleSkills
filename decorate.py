import functools



def logging(func):
    @functools.wraps(func)
    def decorator():
        print("{} called".format(func.__name__))
        result = func()
        print("{} end".format(func.__name__))
        return result
    return decorator


@logging
def test01():
    return 1

print(test01())
print(test01.__name__)        #写一个decorator的时候，最好在实现之前加上functools的wrap，它能保留原有函数的名称和docstring    



#函数可以带参数的修饰器
def logging_2(func):
    functools.wraps(func)
    def decorator(*args,**kwargs):
        print("{} called".format(func.__name__))
        result = func(*args,**kwargs)
        print("{} end".format(func.__name__))
        return result
    return decorator

@logging_2
def test02(a,b):
    print("in function test01,a={},b={}".format(a,b))
    return 1

@logging_2
def test03(a,b,c=1):
    print("in function test03,a={},b={},c={}".format(a,b,c))
    return 1

print(test03(1,2,c=3))    



#修饰器带参数
def params_chack(a_type,b_type):
    def __outer(func):
        @functools.wraps(func)
        def __inner(a,b):
            assert isinstance(a,a_type) and isinstance(b,b_type)
            return func(a,b)
        return __inner
    return __outer


@params_chack(int,(list,tuple))
def test04(a,b):
    print("in function test04, a={},b={}".format(a,b))
    return 1









