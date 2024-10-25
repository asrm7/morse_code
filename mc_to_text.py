def morse_to_text():
    # The dictionary you provided
    morse_code_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', 
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', 
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', 
        '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', 
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', 
        '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', 
        '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', 
        '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@'
    }

    # Asking for input after printing the list
    morse_input = input("\nEnter the Morse code to decode (use ' / ' to separate words): ")

    # Splitting the morse code into words using ' / ' as delimiter
    words = morse_input.split(' / ')
    decoded_message = []

    # Decoding each word
    for word in words:
        # Splitting the word into characters using space as delimiter
        characters = word.split(' ')
        decoded_word = ''.join([morse_code_dict.get(char, '') for char in characters])
        decoded_message.append(decoded_word)

    # Join the decoded words and return the final message
    return ' '.join(decoded_message)

# Example usage:
decoded_message = morse_to_text()
print(f"\nDecoded message: {decoded_message}")
