
message = "  JohnDoe  "
clean_message = message.strip()
print(clean_message)  # JohnDoe

message = "...JohnDoe..."
clean_message = message.strip(".")
print(clean_message)  # JohnDoe

email_content = "Dear Customer, we are happy to serve you.\n"
clean_content = email_content.rstrip("\n")
print(clean_content)

log_entry = "  2023-02-17 10:00:00 System rebooted successfully"
clean_log = log_entry.lstrip()
print(clean_log)  # 2023-02-17 10:00:00 System rebooted successfully

def get_date_from_datetime(datetime_string):
    """Extract date from datetime string in format YYYY-MM-DD HH:MM:SS"""
    if not datetime_string or len(datetime_string) < 10:
        return None
    return datetime_string[:10]

# Test cases
print(get_date_from_datetime("2023-12-01 15:30:00"))  # "2023-12-01"
print(get_date_from_datetime("2024-01-20 08:15:45"))  # "2024-01-20"
print(get_date_from_datetime(None))                    # None
print(get_date_from_datetime(""))                      # None
print(get_date_from_datetime("2024"))                  # None

#Masking sensitive information
card_number = "1234567890123456"
masked_card = "*" * 12 + card_number[-4:]
print("Masked card number:", masked_card) # Masked card number: ************3456

id = "RobertTalbot"
masked_id = "*" * 8 + id[-4:]
print("Masked ID:", masked_id) # Masked ID: ************Talbot
