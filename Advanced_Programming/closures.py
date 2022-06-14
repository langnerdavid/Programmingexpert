'''
class Collection:
    def __init__(self):
        self.lst = []

    def add_value(self, value):
        self.lst.append(value)
        return self.lst



def collection():
    
    lst = []
    
    def inner(value):
        lst.append(value)
        return lst

    return inner

add_value = collection()
print(add_value(1))
print(add_value(2))
print(add_value(3))
'''


#my_set = add_value(1)
#print(set(my_set))

'''
def counter(start):
    count = start

    def increment(value):
        nonlocal count
        count += value
        return count

    return increment


count = counter(2)
print(count(1))
'''

from re import X


def outer():
    def inner():
        #if you put "nonlocal x" here than outer would be 2 as well
        def inner2():
            nonlocal x #nonlocal for inner but not for outer
            x = 2
            print("Inner2: ", x )

        x = 3
        inner2()
        print("Inner: ", x)

    x = 4
    inner()
    print("Outer: ", x)


outer()

#Inner2: 2
#Inner: 2
#Outer: 4