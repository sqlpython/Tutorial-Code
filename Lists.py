# Lists in Python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers) # [5, 4, 3, 2, 1]

# Sorting a List in Python
names = ["Anna", "John", "Bob", "Diana"]
names.sort()
print(names) # ["Anna", "Bob", "Diana", "John"]

# Copying a list in Python
original_list = [1, 2, 3]
copied_list = original_list.copy()
copied_list.append(4)
print("Original List:", original_list) # Original List: [1, 2, 3]
print("Copied List:", copied_list) # Copied List: [1, 2, 3, 4]

# PoP
fruits = ["apple", "banana", "cherry"]
removed_fruit = fruits.pop(1)
print("Removed Fruit:", removed_fruit) # Removed Fruit: banana
print("Remaining Fruits:", fruits) # Remaining Fruits: ["apple", "cherry"]

fruits = ["apple", "banana", "cherry"]
removed_fruit = fruits.pop()
print("Removed Fruit:", removed_fruit) # Removed Fruit: cherry
print("Remaining Fruits:", fruits) # Remaining Fruits: ["apple", "banana"]

def get_reversed_list(items):
    return list(reversed(items))

print(get_reversed_list([1, 2, 3]))  # [3, 2, 1]

def get_reversed_list(items):
    copy = items.copy()
    copy.reverse()
    return copy
print(get_reversed_list([5, 6, 7]))  # [3, 2, 1]
# returns none
def sort_list(items: list) -> None:
    """Sort a list in place in ascending order.
    
    Args:
        items: The list to sort (modified in place)
        
    Returns:
        None (modifies the list in place)
    """
    items.sort()