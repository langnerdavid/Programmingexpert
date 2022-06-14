


def fib(n):
    last = 1
    second_last = 1
    current = 1
    while current <= n:
        num = last + second_last
        yield num

        second_last = last
        last = num
        current += 1


#for val in fib(10):
#    print(val)

'''
fib_numbers = [1,1]
 
for i in range(2, 10):
    last = fib_numbers[i - 1]
    second_last = fib_numbers[i - 2]
    num = last + second_last
    fib_numbers.append(num)

print(fib_numbers)
'''

# Write your code here.
def new_range(start, stop, step):
    rounds = abs(stop - start)
    for i in range(rounds):
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <= stop: 
            break
        yield start
        start += step

iter = new_range(1, 10, 2)
print(list(iter))