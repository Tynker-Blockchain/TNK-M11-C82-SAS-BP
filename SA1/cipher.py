capitalLetters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerLetters='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'

# Define the function cipher() that takes two parameter i.e 'plaintext' and a key 'n'

    # Access globals: capitalLetters, lowerLetters, numbers
    
    # Create empty string variable cipherText
    

    # Loop throught each 'char' in the 'plaintext'
    
        # Check if 'char' is present in 'numnbers' list
        
            # Get the current position of the 'char' in 'numbers' list
            
            # Calculate the character using formula : numbers[(currentPosition + n ) % 10] and add it to cipherText
            
        # Check if 'char' is present in 'lowerLetters' list
        
            # Get the current position of the 'char' in 'lowerLetters' list
            
            # Calculate the character using formula : numbers[(currentPosition + n ) % 26] and add it to cipherText
            
        # Check if 'char' is present in 'capitalLetters' list
        
            # Get the current position of the 'char' in 'capitalLetters' list
            
            # Calculate the character using formula : numbers[(currentPosition + n ) % 26] and add it to cipherText
            
        # Else add the 'char' to 'cipherText'
        
    
    # Return 'cipherText'
    
        
