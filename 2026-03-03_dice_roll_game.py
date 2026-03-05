import random

n = int(input("How many dice do you want to roll? "))
roll_count = 0

while True:          #you can also use this Method   Rolling = True  while Rolling:
    choice = input("Roll the dice? (y/n): ").lower()

    if choice == "y":   # if choice == "y" or choice == "Y" is also valid but used this to get ride of 2nd condition
        roll_count += 1
        print("You rolled:" , end=" ")

        for i in range(n):
            dice = random.randint(1, 6)
            print(f"{dice}", end=" ")

        print()  # new line

    elif choice == "n":
        print(f"Thanks for playing! You rolled {roll_count} times.")
        break

    else:
        print("Invalid choice. Please enter 'y' or 'n'.")
