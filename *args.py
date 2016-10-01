def test(*args):
    for value in args:
        try:
            yield value
        finally:
            print("fuck!")

for i in test(98,99,100,101,201):
    print(i)            
