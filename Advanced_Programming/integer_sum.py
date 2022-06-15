def flatten_lists(func):
    def wrapper(*args):
        individual_arg = []
        #print(*args)
        for item in args:
            if isinstance(item, list):
                for val in item:
                    individual_arg.append(val)
            else:
                individual_arg.append(item)

        #print(individual_arg)
        result = func(*individual_arg)
        #print(result)
        return result

    return wrapper

def convert_strings_to_ints(func):
    def wrapper(*args):
        
        int_list = []

        #for item in args:
        #    if isinstance(item, str) and item.isdigit():
        #        int_list.append(int(item))
        #    else:
        #        int_list.append(item)
        first = list(filter(lambda x: isinstance(x, str) and x.isdigit(), args))
        second = list(filter(lambda x: x, args))
        for i in first:
            int_list.append(int(i))
        for i in second:
            int_list.append(i)

        result = func(*int_list)
        #print(result)
        return result
    return wrapper


def filter_integers(func):
    def wrapper(*args):
        int_list = list(filter(lambda x: isinstance(x, int), args))
        

        result = func(*int_list)
        #print(result)
        return result

    return wrapper


@flatten_lists
@convert_strings_to_ints
@filter_integers
def integer_sum(*args):
    return sum(args)


print(integer_sum(["1", "2", -0.9, 4, [5, "hi", "3"]]))