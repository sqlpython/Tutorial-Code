import os
import math

def make_lemonade(sugar_grams, water_liters):
    # If there's no water, return 
    
#print("\033[H\033[J", end="")
    if water_liters == 0:
        return float("nan")
    

    # Convert liters to milliliters
    water_ml = water_liters * 1000
    
    # Calculate servings based on water (500 ml per serving)
    servings_from_water = water_ml / 500
    
    # Calculate servings based on sugar (100 g per serving)
    servings_from_sugar = sugar_grams / 100
    
    # Return the minimum (limiting factor)
    return min(servings_from_water, servings_from_sugar)

print(make_lemonade(500, 2))    # Output: 4.0 (water limits: 2000/500 = 4)
print(make_lemonade(600, 6))    # Output: 6.0 (sugar limits: 600/100 = 6)
print(make_lemonade(300, 0))    # Output: nan (no water)
print(make_lemonade(100, 0.1, 0))  # Expected: 0