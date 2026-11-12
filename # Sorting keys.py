# Sorting
words = ["banana", "apple", "cherry", "date"]
sorted_words = sorted(words, key=len)
print(sorted_words) # ["date", "apple", "banana", "cherry"]

words = ["banana", "apple", "cherry", "date"]

def half_len(word):
    return len(word) // 2

sorted_words = sorted(words, key=half_len)
print(sorted_words) # ["apple", "date", "banana", "cherry"]
