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


detect_lowercase_words()  # function call
# Add a newline here at the end of the file


