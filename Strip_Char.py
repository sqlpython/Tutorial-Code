print("Welcome to Python!")

message = "  JohnDoe  "
clean_message = message.strip()
print(clean_message) # JohnDoe

message = "...JohnDoe..."
clean_message = message.strip(".")
print(clean_message) # JohnDoe

log_entry = "  2023-02-17 10:00:00 System rebooted successfully"
clean_log = log_entry.lstrip()
print(clean_log) # 2023-02-17 10:00:00 System rebooted successfully

user_input = "   username@example.com   "

#  Write code here
cleaned_input = user_input.strip()
print(cleaned_input)
cleaned_input = user_input.lstrip()
print(cleaned_input)
cleaned_input = user_input.rstrip()
print(cleaned_input)