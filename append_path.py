#对于模块和自己写的程序不在同一个目录下，可以把模块的路径通过sys.path.append(路径)添加到程序中。
import os
import sys
print(sys.path)
print("--------------------------")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
print(sys.path)