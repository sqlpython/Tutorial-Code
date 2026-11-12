# Remove_Else
'''def get_numbers _equality(a: int, b: int) -> str:
    if a == b:
        return "a and b are equal"
    if a < b:
        return "a is less than b"
    return "a is greater than b" '''
#  Simple_Math_Checker
def check_number(number: int) -> list[bool]:
    pass
    """
    Analyzes an integer number based on three criteria.
    
    Args:
        number: An integer to analyze
    
    Returns:
        A list of three boolean values:
        - Index 0: Is the number positive?
        - Index 1: Is the number even?
        - Index 2: Is the number divisible by 10?
    """
    is_positive = number > 0
    is_even = number % 2 == 0
    is_divisible_by_10 = number % 10 == 0
    
    return [is_positive, is_even, is_divisible_by_10]

print(check_number(20))   # [True, True, True]
print(check_number(-3))   # [False, False, False]
print(check_number(7))    # [True, False, False]
