# 具名元祖有两种构建方式

from collections import namedtuple
Person = namedtuple("Person","sex age")
print(type(Person))
zhang = Person("male","22")
print(zhang)


Person = namedtuple("Person",("sex","age"))
print(type(Person))
zhang = Person("male","22")
print(zhang)
