#lst = [(1, 2), (-2, -4), (3, 4), (0, 0)]
#lst.sort(key=lambda x: x[1])
#print(lst)
mul = lambda x: lambda y: x * y

result = mul(2)
#print(result(3))

a = lambda y: lambda x: lambda z: print(x + y, end=z)
print(a("b")("a")("|"))