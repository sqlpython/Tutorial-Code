def get_location(coordinates, commands):
    x, y = coordinates
    
    moves = {
        'forward': (0, 1),
        'back': (0, -1),
        'right': (1, 0),
        'left': (-1, 0)
    }
    
    for cmd in commands:
        dx, dy = moves.get(cmd, (0, 0))
        x += dx
        y += dy
    
    return [x, y]

# Test
print(get_location([0, 0], ["forward", "right"]))  # [1, 1]
print(get_location([0, 5], ["back", "back", "back", "right", "left", "forward"]))  # [0, 3]









