def calculate_compound_interest(p, r, t, n=1):
    """
    p: Principal amount
    r: Annual interest rate (as a decimal, e.g., 0.05 for 5%)
    t: Number of years
    n: Number of times interest is compounded per year
    """
    amount = p * (1 + r/n)**(n * t)
    interest = amount - p
    return amount, interest

# Example calculation
p = 1000
r = 0.05
t = 1

total, earned = calculate_compound_interest(p, r, t)
print(f"Total Amount: ${total:.2f}")
print(f"Interest Earned: ${earned:.2f}")