# Smaller Digits

def find_smaller_digits(ls: list) -> list:
    result = []
    for i in range(len(ls)):
        count = 0
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[i]:
                count += 1
        result.append(count)
    return result

# Test cases
print(find_smaller_digits([5, 4, 3, 2, 1]))  # Output: [4, 3, 2, 1, 0]



