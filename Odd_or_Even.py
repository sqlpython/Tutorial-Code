#def is_even(number: float) -> bool:
    # write your code here
#    pass
def is_even(number: float) -> bool:
    """
    Checks if a number is even.
    
    Args:
        number: A float or integer to check
    
    Returns:
        True if the number is even, False otherwise
    """
    return number % 2 == 0

    print(is_even(2))      # True
print(is_even(3))      # False
print(is_even(0))      # True
print(is_even(-4))     # True
print(is_even(-5))     # False
print(is_even(100))    # True
print(is_even(99))     # False