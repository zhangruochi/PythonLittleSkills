#islice 生成迭代器
from itertools import islice
for item in islice('ABCDEFG', 2, 4):
    print(item)


#迭代器
a= iter([1,2,3])
c = a.__iter__()
print(a)
print(c)

if(a is c):
    print(True)

print(a.__next__())
print(a.__next__())
print(a.__next__())
#print(a.__next__())  #StopIteration                                    bb                                                                    




