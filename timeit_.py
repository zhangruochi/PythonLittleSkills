def test(n):
    i = 0
    for i in range(n):
        i += 1
    return i

setup = '''
def test(n):
    i = 0
    for i in range(n):
        i += 1
    return i
'''       

import timeit
time1 = timeit.timeit(stmt='test(10000)',setup="from __main__ import test", number = 1)
time2 = timeit.timeit(stmt='test(10000)',setup=setup, number = 1)

print(time1)
print(time2)


   