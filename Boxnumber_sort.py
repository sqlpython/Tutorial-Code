def is_sorted(box_numbers):
    # .sort() modifies the list in place and returns None,
    # so we compare a sorted version of the list instead.
    return box_numbers == sorted(box_numbers, reverse=True)

box_numbers = [1, 2, 3, 4, 5]
box_numbers.sort(reverse=True)
print(box_numbers)

box_numbers.sort()
print(box_numbers)
print(is_sorted(box_numbers))

if __name__ == "__main__":
    box_numbers = [1, 2, 3, 4, 5]
    print(is_sorted(box_numbers))
    print(is_sorted([5, 4, 3, 2, 1]))
