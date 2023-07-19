capitalLetters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerLetters='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'
# Create string of special characters


def cipher(plaintext, n):
    # Access specials as global
    global  capitalLetters, lowerLetters, numbers
    ciphertext = ''

    for char in plaintext:
        if char in numbers:
            currentPosition = numbers.find(char)
            ciphertext += numbers[(currentPosition + n ) % 10]
        elif char in lowerLetters:
            currentPosition = lowerLetters.find(char)
            ciphertext += lowerLetters[(currentPosition + n )% 26] 
        elif char in capitalLetters:
            currentPosition = capitalLetters.find(char)
            ciphertext += capitalLetters[(currentPosition + n) % 26]
        # Check if char exits in specials  
        
            # Get position of the char in specials   
            
            # Get the new cha using formula : specials[(currentPosition + n) % 15], and add it to ciphertext
            
        else:
            ciphertext += char

    return ciphertext
        
def decipher(ciphertext, n):
    # Access specials as global
    global capitalLetters, lowerLetters, numbers
    plaintext = ""

    for char in ciphertext:
        if char in numbers:
            currentPosition = numbers.find(char)
            plaintext += numbers[(currentPosition - n) % 10]
        elif char in lowerLetters:
            currentPosition = lowerLetters.find(char)
            plaintext += lowerLetters[(currentPosition - n )% 26] 
        elif char in capitalLetters:
            currentPosition = capitalLetters.find(char)
            plaintext += capitalLetters[(currentPosition - n) % 26] 
        # Check if char exits in specials  
        
            # Get position of the char in specials 
            
            # Get the new cha using formula : specials[(currentPosition - n) % 15], and add it to plaintext
                   
        else:
            plaintext += char
            
    return(plaintext)