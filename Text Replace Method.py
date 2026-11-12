text = "This cat is smaller than that cat."
new_text = text.replace("cat", "dog")
print(new_text) # This dog is smaller than that dog.

text = "This cat is smaller than that cat."
new_text = text.replace("cat", "dog", 1)
print(new_text) # This dog is smaller than that cat.

message = "Hello John Doe. Your current balance is 100$."
new_message = message.replace("John Doe", "Jane Doe").replace("100$", "150$")
print(new_message) # Hello Jane Doe. Your current balance is 150$.

def update_announcement(original_announcement: str, old_place: str, new_place: str) -> str:
    """Replace old venue with new venue in announcement."""
    if not original_announcement or not old_place:
        return original_announcement
    
    return original_announcement.replace(old_place, new_place)

# Test cases
test_cases = [
    ("The meeting will take place in the park.", "park", "cafe", "The meeting will take place in the cafe."),
    ("Don't forget to bring umbrellas, it will rain!", "rain", "sun", "Don't forget to bring umbrellas, it will sun!"),
    ("See you at the park.", "park", "beach", "See you at the beach."),
    ("", "park", "cafe", ""),  # Empty string
]

for announcement, old, new, expected in test_cases:
    result = update_announcement(announcement, old, new)
    status = "✓" if result == expected else "✗"
    print(f"{status} {result}")
    