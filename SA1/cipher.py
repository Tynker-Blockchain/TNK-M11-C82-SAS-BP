capitalLetters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerLetters='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'

def cipher(plaintext, n):
    global  capitalLetters, lowerLetters, numbers
    cipherText = ''

    for char in plaintext:
        if char in numbers:
            currentPosition = numbers.find(char)
            cipherText += numbers[(currentPosition + n ) % 10]
        # Check if 'char' is present in 'lowerLetters' list
        
            # Get the current position of the 'char' in 'lowerLetters' list
        
            # Calculate the character using formula : numbers[(currentPosition + n ) % 26] and add it to cipherText
         
        # Check if 'char' is present in 'capitalLetters' list
        
            # Get the current position of the 'char' in 'capitalLetters' list
        
            # Calculate the character using formula : numbers[(currentPosition + n ) % 26] and add it to cipherText
             
        else:
            cipherText += char
    
    return cipherText
        
