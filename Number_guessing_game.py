#generate the random number
#Loop
 #Ask the user to make a guess
 #if not a valid number
   #print error message
 #if number < guess
  #   print too low
 #if number > guess
  #  print too high
 #else
  #  print well done

import random
while True:
    try:
        start_Value = int(input("Enter the Start value for the range: "))
        end_Value = int(input("Enter the end value for the range: "))
        number_to_guess = random.randint(start_Value,end_Value)
        break
    except ValueError:
        print("Please enter the valid number. ")
count = 5
attempts = 0

while True:
    try:
       
        guess = int(input(f"Guess the number between {start_Value} and {end_Value}: "))
        count -= 1
        attempts += 1
     
        
            
        if guess < number_to_guess:
            print("Too low!")

        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
             
            
            
        if count == 0:
            print(f"Sorry your attempts are over the number you have to guess is {number_to_guess}")
            break
        print(f"you have {count} chances left to guess the number")

    except ValueError:
        print("Please enter a valid number")
    

