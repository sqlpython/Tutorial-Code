import re

def calculate_guests(guests_input: str) -> int | str:
    """Extract the first integer from guests input string.
    
    Returns:
        int: The first integer found in the string
        str: "not a number" if no integer found or if it's 0
    """
    # Find all integers in the string
    numbers = re.findall(r'\d+', guests_input)
    
    # If no numbers found, return "not a number"
    if not numbers:
        return "not a number"
    
    # Convert first number to int
    first_number = int(numbers[0])
    
    # If number is 0, return "not a number"
    if first_number == 0:
        return "not a number"
    
    return first_number

print(calculate_guests("I think 5 guests"))  # 5
print(calculate_guests("Big company of 15 dudes"))  # 15
print(calculate_guests("5"))  # 5
print(calculate_guests("alone"))  # "not a number"
print(calculate_guests("0"))  # "not a number"
print(calculate_guests("Hello, 9.75 people"))  # 9
print(calculate_guests("There will be 7 or 9 guys"))  # 7
print(calculate_guests("hello cat walks on my keyboard ksadjfhskaj12.34kasdfhsjk"))  # 12

print("Without Regex\n")
def calculate_guests(guests_input: str) -> int | str:
    """Extract first integer without using regex."""
    current_number = ""
    
    for char in guests_input:
        if char.isdigit():
            current_number += char
        elif current_number:
            # Stop at first complete number
            break
    
    if not current_number:
        return "not a number"
    
    first_number = int(current_number)
    
    if first_number == 0:
        return "not a number"
    
    return first_number


print(calculate_guests("I think 5 guests"))  # 5
print(calculate_guests("Big company of 15 dudes"))  # 15
print(calculate_guests("5"))  # 5
print(calculate_guests("alone"))  # "not a number"
print(calculate_guests("0"))  # "not a number"
print(calculate_guests("Hello, 9.75 people"))  # 9
print(calculate_guests("There will be 7 or 9 guys"))  # 7
print(calculate_guests("hello cat walks on my keyboard ksadjfhskaj12.34kasdfhsjk"))  # 12
