"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

    
"""
Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
"""
    # write your code inside this function.
guess = random.randint(1,10)
print("-"* 50) 
print("Welcome to the number guessing Game!!! ")
print("-"* 50)
print("Ready to play: ")


def start_game():
    
    ran_number = 0
    num_count = 0
    
    
    try:
        while ran_number != guess:
            ran_number = int(input("Type a number between 1 and 10: "))
            num_count += 1
            
            if ran_number > guess:
                print("Sorry, It's lower")
                
            elif ran_number < guess:
                print("Sorry,It's higher ")
                
                
            else:
                print("Congs You have got it")
                print("It took you {} tries \n".format(num_count))
                print("Thank you for playing with us!!!!! \n")
                print("*"* 20) 
                print("END OF GAME...")
                print("*"* 20) 
                
                
        
    except Exception:
            print("Sorry Can you please enter a figure number like 1 " )
            start_game()
            
    

#if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    
start_game()

