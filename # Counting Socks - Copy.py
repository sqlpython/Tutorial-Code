# Counting Socks
def count_matching_socks(colors: list) -> int:
    from collections import Counter
    
    color_counts = Counter(colors)
    pairs = 0
    
    for count in color_counts.values():
        pairs += count // 2  # Each pair requires 2 socks
    
    return pairs

count_matching_socks([10, 10])  # 1 pair of socks with color 10
count_matching_socks([2, 2, 2, 2, 2])  # 2 pairs of socks with color 2
count_matching_socks([10, 20, 30, 40, 50, 60])  # 0 pairs, all socks have different colors
count_matching_socks([10, 20, 30, 10, 20, 60])  # 2 pairs, one of color 10 and one of color 20
