# Function Advanced

def make_coffee(size: str, coffee_type: str = "regular", sugar: int = 2) -> str:
    return f"Making a {size} cup of {coffee_type} coffee with {sugar} sugar(s)."

print(make_coffee("large")) # Making a large cup of regular coffee with 2 sugar(s).


def prepare_dinner(*guests):
    print(f"Preparing dinner for {len(guests)} guests.")
    for guest in guests:
        print(f"Welcome, {guest}!")

prepare_dinner("Alex", "Taylor")


def configure_app(**kwargs):
    """
    Configures an application with various settings.
    """
    config = {
        "debug": False,
        "port": 8000,
        "host": "localhost"
    }
    
    # Update config with provided kwargs
    config.update(kwargs)
    
    return config

# Using the function
app_config = configure_app(debug=True, port=3000, timeout=30)
print(app_config)
# Output: {'debug': True, 'port': 3000, 'host': 'localhost', 'timeout': 30}


def multiply_numbers(*args, **kwargs):
    """
    Multiplies two numbers a and b.
    
    Args:
        *args: Positional arguments (first is a, second is b)
        **kwargs: Keyword arguments (can include 'a' and 'b')
    
    Returns:
        The product of a and b (defaults to 1 if not provided)
    """
    # Extract 'a' from positional arguments or keyword arguments
    a = args[0] if len(args) > 0 else kwargs.get('a', 1)
    
    # Extract 'b' from positional arguments or keyword arguments
    b = args[1] if len(args) > 1 else kwargs.get('b', 1)
    
    return a * b

# Example usage
result1 = multiply_numbers(3, 4)  # Using positional arguments
result2 = multiply_numbers(a=5, b=6)  # Using keyword arguments
print(result1)  # Output: 12
print(result2)  # Output: 30

