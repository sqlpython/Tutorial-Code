total_savings = 0
current_savings = 200
monthly_bonus = 30

for month in range(1, 7):
    total_savings += current_savings + monthly_bonus
    print(f"Month {month}: Total savings so far ${total_savings}")

print(f"After 6 months, you have saved ${total_savings} for your vacation!")
