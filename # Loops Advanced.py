# Loops Advanced

books = ["The Clean Coder", "Fiction Story", "Pragmatic Programmer", "Holiday Adventure", "Learn Python the Hard Way"]
for book in books:
    if "Fiction" in book or "Adventure" in book:
        continue
    print(f"Adding to professional development list: {book}")

def check_emails_against_blacklist(emails, blacklist):
    """
    Check if any email in the list is in the blacklist.
    
    Args:
        emails (list): List of email addresses to check
        blacklist (set): Set of blacklisted email addresses
    
    Returns:
        str: The first blacklisted email found, or empty string if none found
    """
    for email in emails:
        if email in blacklist:
            return email
    return ""
print(check_emails_against_blacklist(["user@example.com", "admin@company.com"], {"admin@company.com"}))

while True:
    user_input = input("Enter \"exit\" to stop the program: ")
    if user_input.lower() == "exit":
        break
    print(f"You entered: {user_input}")

import random
import time

while True:
    server_command = random.choice(["running", "stop"])
    if server_command == "stop":
        print("Server is shutting down.")
        break
    else:
        print("Server is running smoothly.")
    time.sleep(5)
exit

# Lower Case
def detect_lowercase_words():
    """
    Continuously reads words from user input and detects lowercase words.
    Stops when the user enters 'exit'.
    """
    while True:
        word = input()
        
        if word == "exit":
            break
        
        if word.islower():
            print(f"{word} detected")