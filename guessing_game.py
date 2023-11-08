import random

print("welcome to the number guessing game!")
print("I'm guessing a number between 1 and 100 both inclusive")
chosen_number = random.randint(1, 101)
difficulty = input("choose difficulty 'easy' or 'hard'\n")
if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5
print(f"you have {attempts} attempts to guess the number")

guess = 0
while attempts > 0 and guess != chosen_number:
    guess = int(input("make a guess\n"))
    if guess == chosen_number:
        print("you have guessed right\n you won")
        break
    elif guess > chosen_number:
        print("Too high")
    else:
        print("Too low")
    attempts -= 1
    if attempts == 0:
        print("you have run out of attempts\n you lose")
        break
    else:
        print(f"you have {attempts} attempts remaining")

