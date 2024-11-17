def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypt or decrypt a text using the Caesar cipher.
    
    Parameters:
        text (str): The input text.
        shift (int): The number of positions to shift.
        mode (str): Either 'encrypt' or 'decrypt'. Defaults to 'encrypt'.
    
    Returns:
        str: The encrypted or decrypted text.
    """
    if mode == 'decrypt':
        shift = -shift
    
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result


# Example usage:
if __name__ == "__main__":
    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))
    mode = input("Mode ('encrypt' or 'decrypt'): ").strip().lower()
    
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode! Choose 'encrypt' or 'decrypt'.")
    else:
        result = caesar_cipher(text, shift, mode)
        print(f"Result: {result}")
