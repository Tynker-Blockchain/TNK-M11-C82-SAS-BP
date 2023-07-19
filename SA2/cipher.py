capitalLetters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerLetters='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'

def cipher(plaintext, n):
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
        else:
            ciphertext += char

    return ciphertext
        
# Define the function decipher() that takes two parameter i.e 'ciphertext' and a key 'n'

    # Access globals: capitalLetters, lowerLetters, numbers
    
    # Create empty string variable plaintext
    

    # Loop throught each 'char' in the 'ciphertext'
    
        # Check if 'char' is present in 'numnbers' list
        
            # Get the current position of the 'char' in 'numbers' list
            
            # Calculate the character using formula : numbers[(currentPosition - n) % 10] and add it to plaintext
            
        # Check if 'char' is present in 'lowerLetters' list
        
            # Get the current position of the 'char' in 'lowerLetters' list
            
            # Calculate the character using formula : lowerLetters[(currentPosition - n )% 26] and add it to plaintext
            
        # Check if 'char' is present in 'capitalLetters' list

            # Get the current position of the 'char' in 'capitalLetters' list
            
            # Calculate the character using formula : capitalLetters[(currentPosition - n) % 26] and add it to plaintext
            
            
        # Else add the 'char' to 'plaintext'
        

    # Return 'plaintext'
    