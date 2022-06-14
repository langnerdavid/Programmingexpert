#def sum_items(*args, **kwargs): #any number of arguments
#    print(args)
#    print(kwargs)
#
#sum_items(1,2,3, a=2, l=5)
#sum_items(1,2,3,4,5)

#def sum_items(p1, p2, a=None, b=None, c=None):
#    return a + b + c + p1 + p2

#args = [4, 5, 7]
#x = sum_items(*args)  #splits the list in individual items (works with sring, tuples as well)
#print(x)
#args = [1, 2]
#kwargs = {"a": 5, "b": 10, "c": 5}
#x = sum_items(*args, **kwargs) #** splits dictionary 

#values = [1,2,3,4,5,6,7,8,9,10]
#print(*values)

def test(p1, *args, **kwargs):
    print(p1, args, kwargs)

values = [1,2,3,4,5,6]
kwargs = {"s": 1, "hello": 4, "k": True}
test(4, *values, **kwargs)