import random

while True:
    choices = ('r','p','s')
    emojis = {'r':'🪨','p':'📃','s':'✂️'}

    user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid choice!")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie")

    elif ((user_choice=='r' and computer_choice == 's') or
         (user_choice == 's' and computer_choice == 'p') or 
         (user_choice == 'p' and computer_choice == 'r')):
        print("You Won")
    else:
        print("You lose")

    while True:
        should_continue = input("Press 'y' to continue or 'n' to exit: ").lower()

        if should_continue == 'y':
            break   # break this small loop and continue game
        elif should_continue == 'n':
            exit()
        else:
            print("Invalid input! Please enter 'y' or 'n'")
    
   







