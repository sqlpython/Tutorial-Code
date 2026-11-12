def mask_card_number(card_number: str) -> str:
    #  Write code here
    return (card_number)
    pass
"""card_number = "1234 5678 901 3456"
masked_card = ("*" * 4 ) + " " + ("*" * 4 ) +  " " +  ("*" * 4 ) + " " card_number:[-4]
print({card_number})
print(f"Masked card number:", {masked_card}) # Masked card number: ************3456 """
card_number = "1234 5678 9012 3456"
print(f'Original card number: {card_number}')
# Method 1: Simple and clear
masked_card = "**** **** **** " + card_number[-4:]
print(f"Masked card number: {masked_card}")
# Output: **** **** **** 3456