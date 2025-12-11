def morse_to_english(morse_code):
    # Dictionary mapping Morse code to characters
    morse_code_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', 
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', 
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', 
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', 
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', 
        '--..': 'Z',
        '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', 
        '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', 
        '--..--': ',', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-', 
        '-.--.': '(', '-.--.-': ')'
    }

    morse_code = morse_code.strip() # Remove extra whitespace from ends
    decoded_message = []

    # Step 1: Split the Morse code by '/' to separate words
    # (Assuming '/' is used as a word separator)
    words = morse_code.split('/')

    for word in words:
        decoded_word = []
        # Step 2: Split each word by space ' ' to get individual characters
        chars = word.strip().split(' ')
        
        for char in chars:
            if char in morse_code_dict:
                decoded_word.append(morse_code_dict[char])
            elif char == '':
                continue # Skip empty strings resulting from extra spaces
            else:
                decoded_word.append('?') # Placeholder for unknown codes
        
        # Join characters to form the word and add to the message list
        decoded_message.append("".join(decoded_word))

    # Step 3: Join all words with a normal English space
    return " ".join(decoded_message)

# --- Main Execution ---
if __name__ == "__main__":
    # Example input: "HELLO WORLD" in Morse
    sample_input = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    
    print("Enter Morse Code (use space for char separation and '/' for word separation):")
    user_input = input().strip() or sample_input # Uses sample if input is empty
    
    result = morse_to_english(user_input)
    
    print("\nInput Morse:   ", user_input)
    print("Decoded Text:  ", result)