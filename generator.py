a = range(100000)

generator = ( x*2 for x in a )
print(type(generator)) #<class 'generator'>

for i in generator:
    print(i)


def generator_func(c):
    for i in range(c):
        yield i ** 2

for i in generator_func(10):
    print(i)        

