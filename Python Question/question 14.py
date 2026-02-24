#Check whether a character is digit or alphabet.
def check_char_type(char):
    if len(char) != 1:
        return "Invalid input"
    
    if char.isalpha():
        return "Alphabet"
    elif char.isdigit():
        return "Digit"
    else:
        return "Invalid input"

# Example usage
char = '7'
result = check_char_type(char)
print(f"Character: {char}, Type: {result}")