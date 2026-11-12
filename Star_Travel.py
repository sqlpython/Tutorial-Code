# Star_Travel
distance_light_years = 2.537 * 1_000_000
distance_km = distance_light_years * 9_461_000_000_000
speed_of_light_km_per_s = 300_000

#  Write code here
# Given values
distance_light_years = 2.537e6  # 2.537 million light-years
light_year_km = 9.461e12  # 1 light-year in kilometers
speed_of_light = 300000  # km/s
seconds_per_year = 31536000  # seconds in a year

# Calculate distance in kilometers
distance_km = distance_light_years * light_year_km
print(f"Distance: {distance_km:.3e} km")

# Calculate time in seconds
time_in_seconds = distance_km / speed_of_light
print(f"\nTime in seconds: {time_in_seconds:.3e} seconds")
print(f"Time in seconds: {time_in_seconds:,.0f} seconds")

# Calculate time in years
time_in_years = time_in_seconds / seconds_per_year
print(f"\nTime in years: {time_in_years:,.0f} years")
print(f"Time in years: {time_in_years:.3e} years")

