
def generate_string(string, frequency):
    for i in string:
        for k in range(frequency):
            yield i


class GenerateString:
    def __init__(self, string, frequency):
        self.string = string
        self.frequency = frequency

    def __iter__(self):
        self.current_index = 0
        self.current_freq = 0
        return self

    def __next__(self):
        if self.current_freq > self.frequency:
            self.current_index += 1
            self.current_freq = 0
            
        if self.current_index >= len(self.string):
            raise StopIteration
        

        self.current_freq += 1
        return self.string[self.current_index]
        




