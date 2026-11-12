# Leaders

def get_leaders(numbers: list) -> list:
    leaders = []
    right_sum = 0
    
    # Traverse from right to left
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] > right_sum:
            leaders.append(numbers[i])
        right_sum += numbers[i]
    
    # Reverse to maintain original order
    return leaders[::-1]

# Print the leaders
result = get_leaders([1, 2, 3, 4, 0])
print(result)
