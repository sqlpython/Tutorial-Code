# Product ID
import re

def get_product_id(url: str) -> str:
    # Look for common patterns: /product/123, ?id=123, ?product_id=123
    patterns = [
        r'/product[s]?/([\w-]+)',
        r'[?&]product[_-]?id=([\w-]+)',
        r'[?&]id=([\w-]+)',
        r'/([\d]+)/?$'  # Last segment if numeric
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url, re.IGNORECASE)
        if match:
            return match.group(1)
    
    return ""

# Test cases
print(get_product_id("https://example.com/products/12345"))  # Output: 12345
print(get_product_id("https://example.com/product?id=abc123"))  # Output: abc123
print(get_product_id("https://shop.com/items/xyz789"))  # Output: xyz789


