def sum_dicts(*dicts):
    result = {}
    for d in dicts:
        for key, value in d.items():
            result[key] = result.get(key, 0) + value
    return result

# The examples
empty = {}
assert sum_dicts() == {}
assert sum_dicts(empty) == {}

first = {"a": 2, "b": 4}
second = {"a": 2, "b": 10}
third = {"d": -5}

assert sum_dicts(first) == {"a": 2, "b": 4}
assert sum_dicts(first, third) == {"a": 2, "b": 4, "d": -5}
assert sum_dicts(first, second, third) == {"a": 4, "b": 14, "d": -5}

print("All tests passed!")


# Count letters in a string

def count_letters_in_string(string):
    result = {}
    for letter in string:
        if letter.lower().isalpha():
            result[letter.lower()] = result.get(letter.lower(), 0) + 1
    return result
print(count_letters_in_string('monkeys'))

# Test cases
assert count_letters_in_string("monkeys") == {"m": 1, "o": 1, "n": 1, "k": 1, "e": 1, "y": 1, "s":1} 

# assert count_letters_in_string("aaa") == {"a": 3}
# assert count_letters_in_string("") == {}
# assert count_letters_in_string("123!@#") == {}
# assert count_letters_in_string("Hello World!") == {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}


print("All tests passed!")
