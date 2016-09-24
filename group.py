d1={'name':'zhangsan','age':20,'country':'China'}
d2={'name':'wangwu','age':19,'country':'USA'}
d3={'name':'lisi','age':22,'country':'JP'}
d4={'name':'zhaoliu','age':22,'country':'USA'}
d5={'name':'pengqi','age':22,'country':'USA'}
d6={'name':'lijiu','age':22,'country':'China'}

lst = [d1,d2,d3,d4,d5,d6]

from operator import itemgetter
from itertools import groupby

lst.sort(key = itemgetter("country"))
lstg = groupby(lst,itemgetter("country"))

for key,groups in lstg:
    for group in groups:
        print(key,group)

#print( dict([ (key,list(group)) for key,group in lstg]))
