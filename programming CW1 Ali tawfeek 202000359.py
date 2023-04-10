#importing necessary libraries
import random
import string
import hashlib

#defining the reduction function 
def reduce(password, chain_length): 

    #creating a new string to store the reduced password 
    reduced_password = "" 

    #looping through the characters in the password and reducing them 
    for i in range(chain_length): 

        #getting the character at index i from the password and converting it to an integer 
        char = ord(password[i]) 

        #reducing the character by subtracting 32 from it and converting it back to a character 
        reduced_char = chr(char - 32)  

        #appending the reduced character to the reduced password string  
        reduced_password += reduced_char  

    return reduced_password  

# defining a function to generate random passwords of fixed length  
def generate_passwords(length):  

    # creating an empty list to store all generated passwords  
    passwords = []  

    # looping through all possible combinations of lowercase letters of length 'length' and appending them to 'passwords' list  
    for i in range(3**length):  

        password = ""  

        for j in range(length):  

            char = chr(97 + (i // (26 ** j)) % 26)  

            password += char  

        passwords.append(password)  

    return passwords    
                   
def main():  
    print("Welcome! This program creates a rainbow table of randomly generated passwords hashed using a one-way hash function.") 
    print() 
    # getting input from user about length of each password 
    length = int(input("Please enter desired length of each password: ")) 
    print() 
    chain_length = int(input("Please enter desired chain length: ")) 
    print() 
    # generating all possible combinations of lowercase letters of given length using generate_passwords() function
    passwords = generate_passwords(length) 
    print("Generating rainbow table...") 
    rainbowTable = []
    start_password = "" 
    end_password = "" 
 
    # looping through all generated passwords 
    for i in range(len(passwords)): 
        start_password = end_password 
        end_password = passwords[i] 
        hashedPassword = hashlib.sha256((end_password).encode('utf-8')).hexdigest()
        rainbowTable.append([start_password, end_password, hashedPassword]) 
        
    print("Rainbow Table Generated!") 
    print(rainbowTable)
    print()
    for i in rainbowTable:
        print(f"Start password: {i[0]}", f"End password: {i[1]}", f"First hash: {i[2]}")
    
    
    
    
    while True:
        userHashInput= input("Please enter your hash: ") 
        foundFlag= False 
        for row in rainbowTable:
            if row[2] == userHashInput:
                foundFlag= True
                print("The corresponding plaintext is", row[1])
                break 
            
        if foundFlag == False: 
            print("No match found") 
        choice= input("Do you want to search another hash? (y/n): ") 
        if choice.lower() == 'n': 
            break
            
if __name__ == '__main__':
    main()
