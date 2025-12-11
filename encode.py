def english_to_morse(text):
    # Dictionary mapping characters to Morse code
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
        'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', 
        ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
        '(': '-.--.', ')': '-.--.-', ' ': '/'
    }

    text = text.upper()  # Convert input to uppercase
    morse_output = []

    for char in text:
        if char in morse_code_dict:
            morse_output.append(morse_code_dict[char])
        else:
            # If character is not found, keep it as is or ignore
            # Here we mark unknown characters with '?'
            morse_output.append('?')

    # Join the list with spaces to separate characters
    return ' '.join(morse_output)

# --- Main Execution ---
if __name__ == "__main__":
    user_input = input("Enter text to convert to Morse Code: ")
    result = english_to_morse(user_input)
    
    print("\nOriginal Text:", user_input)
    print("Morse Code:   ", result)