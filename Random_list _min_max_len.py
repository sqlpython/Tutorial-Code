Copyimport random

def generate_random_list(min_value, max_value, length):
    
    """
    Generate a list of random integers within a specified range.
   
    Args:
        min_value: Lower bound (inclusive)
        max_value: Upper bound (inclusive)
        length: Length of the list to generate
    
    Returns:
        A list of random integers between min_value and max_value
    """
    return [random.randint(min_value, max_value) for _ in range(length)]


# Test cases
print(generate_random_list(1, 1, 1))      # [1]
print(generate_random_list(1, 3, 5))      # Example: [2, 3, 1, 1, 3]
print(generate_random_list(10, 20, 3))    # Example: [15, 12, 19]
print(generate_random_list(1, 100, 10))   # Example: [45, 23, 89, 12, ...]