
import math

#lst = [1, 2, 3, 4, 5, 6]
#new_list = list(map(lambda x: math.sqrt(x), lst))    

lst = [[1,2,3], [4,5,6], [7,8,9]]
#new_list = list(map(lambda x: sum(x), lst))

#new_list = list(filter(lambda x: sum(x) > 7, lst))

new_list = filter(lambda y: y % 2 == 0, (map(lambda x: sum(x), lst)))

print(list(new_list))

lst = ["algoexpert", "is", "the", "best"]
x = map(len, lst)
print(list(x))