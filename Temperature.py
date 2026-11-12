def temperature(value):
    #  Write code here
    pass

    if value < 20:
        return "Cold"
    elif 20 <= value <= 50:
        return "Warm"
    else:
        return "Hot"

# Example Usage:
print(f"15 degrees is: {temperature(15)}")
print(f"35 degrees is: {temperature(35)}")
print(f"50 degrees is: {temperature(50)}")
print(f"70 degrees is: {temperature(70)}")
