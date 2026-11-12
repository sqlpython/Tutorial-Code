# Product_ID.p

def get_product_id(url: str) -> str:

    # Remove the .html extension
    url_without_ext = url.rsplit('.html', 1)[0]
    
    # Remove the last 8 characters (8-digit date)
    url_without_date = url_without_ext[:-8]
    
    # Find the last occurrence of 'p' (marks start of product ID)
    last_p_index = url_without_date.rfind('p')
    
    # Extract product ID (everything after the 'p')
    product_id = url_without_date[last_p_index + 1:].strip('-')
    
    return product_id

    # Test cases
test_cases = [
    ("https://exampleshop.com/blue-shirt-p12345-20231215.html", "12345"),
    ("https://exampleshop.com/red-pants-p999-20220101.html", "999"),
    ("https://exampleshop.com/product-name-p42-20231225.html", "42"),
    ("https://exampleshop.com/apple-iphone-p1234567890123456-20240101.html", "1234567890123456"),
    ("https://exampleshop.com/p-shaped-item-p777-20230515.html", "777"),  # 'p' in name
    ("https://exampleshop.com/item123-p456-20231010.html", "456"),  # digits in name
]

print("Testing get_product_id function:")
print("=" * 70)

for url, expected in test_cases:
    result = get_product_id(url)
    status = "✓ PASS" if result == expected else "✗ FAIL"
    print(f"{status}")
    print(f"  URL: {url}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print()


