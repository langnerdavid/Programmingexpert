'''x = [1, 2, 3]

x_iter = x.__iter__()
#iter(x)

while True:
    try:
        #print(next(x_iter))
        print(x_iter.__next__())
    except StopIteration:
        break'''




class Numbers:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.current = 0

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        self.current += 1
        if self.current == 1:
            return self.num1
        elif self.current == 2:
            return self.num2
        elif self.current == 3:
            return self.num3
        else:
            raise StopIteration
#
#nums = [1,2,3]
#for val in nums:
#    print(val)
#

'''class NumberIterator:
    def __init__(self, one, two, three):
        self.one = one  
        self.two = two
        self.three = three
        self.current = 0

    def __next__(self):
        self.current += 1
        if self.current == 1:
            return self.one
        elif self.current == 2:
            return self.two
        elif self.current == 3:
            return self.three
        else:
            raise StopIteration'''


class Range:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = 0
    
    def __iter__(self):
        self.val = self.start
        return self

    def __next__(self):
        
        
        if self.val >= self.stop and self.step > 0:
            raise StopIteration
        elif self.step < 0 and self.val <= self.stop:
            raise StopIteration
        
        #if self.current != 0:
        #    self.val += self.step
        #    return self.val
        
        
        
        if self.current == 0:
            self.current += 1
            return self.start
        self.val += self.step
        return self.val - self.step
        

r = Range(1,5,1)
for x in r:
    print(x)


