# Rowing slices

def row_weights(row: list) -> list:
    team1 = 0
    team2 = 0
    
    for i, weight in enumerate(row):
        if i % 2 == 0:  # Even index (0, 2, 4, ...) goes to team 1
            team1 += weight
        else:  # Odd index (1, 3, 5, ...) goes to team 2
            team2 += weight
    
    return [team1, team2]

# Test cases
print(row_weights([10]))  # [10, 0]
print(row_weights([10, 85, 90]))  # [100, 85]
print(row_weights([8, 5, 9, 3]))  # [17, 8]

