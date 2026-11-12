# Get Leaders

def get_leaders(votes: list) -> list:
    leaders = []
    right_sum = 0
    
    # Traverse from right to left
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] > right_sum:
            leaders.append(numbers[i])
        right_sum += numbers[i]
    
    # Reverse to maintain original order
    return leaders[::-1]

    get_leaders([1, 2, 3, 4, 0]) == [4]   

print(leaders([1, 2, 3, 4, 0]))  # Output: [4]
