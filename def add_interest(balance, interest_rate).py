def add_interest(balance, interest_rate):
    """
    Calculates the new balance after applying annual simple interest for 1 year.

    Args:
        balance (float): The principal amount of money.
        interest_rate (float): The annual interest rate as a percentage (e.g., 5 for 5%).

    Returns:
        float: The new balance after adding the interest.
    """
    # Convert the percentage rate to a decimal for calculation
    rate_decimal = interest_rate / 100.0
    # Time period is 1 year
    time = 1

    # Calculate the simple interest using the formula: SI = P * R * T
    interest_earned = balance * rate_decimal * time

    # Calculate the new balance
    new_balance = balance + interest_earned

    return new_balance

# --- Example Usage ---
initial_balance = 1000.0
annual_rate = 5.0 # 5% interest rate
final_balance = add_interest(initial_balance, annual_rate)

print(f"Initial Balance: ${initial_balance:,.2f}")
print(f"Interest Rate: {annual_rate}%")
print(f"New Balance after 1 year: ${final_balance:,.2f}")