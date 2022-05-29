def get_freq(string):
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def is_string_possible(frequencies, freq_string):
    for freq in freq_string:
        if len(frequencies) > 0:
            if freq_string[freq] > frequencies[freq]:
                return False

    return True
    

def create_both(freq1, freq2):
    both = freq1.copy()
    for key in freq2:
        if key in freq1:
            both[key] += freq2[key]
        else:
            both[key] = freq2[key]
    return both

def create_strings_from_characters(frequencies, string1, string2):
    freq_1 = get_freq(string1)
    freq_2 = get_freq(string2) 
    both = create_both(freq_2, freq_1)

    if not is_string_possible(frequencies, freq_1) and not is_string_possible(frequencies, freq_2):# or len(frequencies) == 0:
        return 0

    if is_string_possible(frequencies, both):
        return 2

    return 1


frequencies = {}    
string1 = "aaabbbc"    
string2 = "bbccde"


print(create_strings_from_characters(frequencies, string1, string2))