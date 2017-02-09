class Test:
    x = 1


test1 = Test()
test2 = Test()

print test1.x
test1.x = 10
print test1.x

print ""

print Test.x
print test2.x


print ""

Test.x = 100
print test1.x
print test2.x    



"""
1
10

1
1

10
100
"""