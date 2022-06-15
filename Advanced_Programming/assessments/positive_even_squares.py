

def positive_even_squares(*args):
    new_lst = []
    for lst in args:
        new_lst += lst

    #print(new_lst)

    even_ints = list(filter(lambda x: x % 2 == 0 and x > 0, new_lst))
    squares = list(map(lambda x: x ** 2, even_ints))
    #print(even_ints)
    return squares







i = positive_even_squares([-5, 2, 3, 4, 5], [1, 3, 5, 6, 7], [-9, -8, 10])
