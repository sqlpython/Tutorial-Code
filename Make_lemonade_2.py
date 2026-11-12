



run_all_edge_case_tests():
    """Run all edge case tests"""
    test_cases = [
        # (sugar, water, description)
        (100, 0.5, "Minimum valid"),
        (99, 1, "Sugar below minimum"),
        (100, 0.4, "Water below minimum"),
        (0, 0, "Both zero"),
        (-100, 1000, "Negative sugar"),
        (1000, -5, "Negative water"),
        (10000, 1, "Water-limited"),
        (100, 10000, "Sugar-limited"),
        (500, 2.5, "Perfect balance"),
        (1000000, 5000000, "Very large numbers"),
        (199, 1000, "Off-by-one low"),
        (200, 1000, "Off-by-one exact"),
    ]
    
    print("=" * 60)
    print("EDGE CASE TEST SUITE")
    print("=" * 60)
    
    for sugar, water, desc in test_cases:
        print(f"\n[TEST] {desc}")
        print(f"Input: sugar={sugar}g, water={water}L")
        result = make_lemonade(sugar, water)
        print(f"Result: {result} servings")
        print("-" * 60)
print(f"{make_lemonade(800, 0)}")
print(f"{make_lemonade(200, 1000)}")
print(f"{make_lemonade(1000, 5000)}")
print(f"{make_lemonade(99, 500)}")
# print(f"\nTotal servings: {result}")