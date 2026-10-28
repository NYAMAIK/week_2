from random import randint, random

secret_number = randint(1, 100)

print("=== GUESS THE NUMBER GAME ===")
print("\nI am thinking of a number between 1 and 100.")
print("\nChoose your difficulty:")
print("1. Easy - 10 tries")
print("2. Medium - 7 tries")
print("3. Hard - 5 tries")

difficulty = input("Enter 1, 2, or 3: ")

if difficulty == "1":
    max_attempts = 10
    level = "Easy"
elif difficulty == "2":
    max_attempts = 7
    level = "Medium"
elif difficulty == "3":
    max_attempts = 5
    level = "Hard"
else:
    print("Invalid choice. Defaulting to Medium Level.")
    max_attempts = 7
    level = "Medium"

attempts = 0
while True:
    guess = int(input("\nEnter your guess: "))
    attempts += 1
    if guess == secret_number:
        print("\nCongratulations! You've guessed the correct number.")
        print(f"It took you {attempts} attempts.")
        break
    elif guess < secret_number:
        print("\nToo low! Try again.")    
    else:
        print("\nToo high! Try again.")
    remaining_attempts = max_attempts - attempts
    if remaining_attempts > 0:
        print(f"\nYou have {remaining_attempts} attempts left.")  
    else:
        print("\nGame Over!")
        print("Sorry, you've run out of attempts. The correct number was:", secret_number)
        break
