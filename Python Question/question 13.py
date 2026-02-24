#Check whether a character is vowel or consonant.
def check_vowel_or_consonant(char):
    if len(char) != 1 or not char.isalpha():
        return "Invalid input"
    
    vowels = "aeiouAEIOU"
    if char in vowels:
        return "Vowel"
    else:
        return "Consonant"

# Example usage
char = 'E'
result = check_vowel_or_consonant(char)
print(f"Character: {char}, Type: {result}")