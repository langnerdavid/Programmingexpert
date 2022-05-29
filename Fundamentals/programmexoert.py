import random

# Write your code here.
# Make sure to use `random.randint` to pick your random number.


while True:
    start = input("Enter the start of the range: ")
    if start.isdigit():
        start = int(start)
        break
    print("Please enter a valid number.")
    
while True:
    stop = input("Enter the end of the range: ")
    if stop.isdigit() and int(stop) > start:
        stop = int(stop)
        break
    print("Please enter a valid number.")

rand = random.randint(start, stop)

count = 0

while True:
    guess = input("Guess a number: ")
    if not guess.isdigit():
        print("Please enter a valid number.") 
    else:
        count += 1
        guess = int(guess)
        if guess == rand and count > 1:
            print(f"You guessed the number in {count} attempts.")
            break
        elif guess == rand and count == 1:
            print("You guessed the number in 1 attempt.")
       