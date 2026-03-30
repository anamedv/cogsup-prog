# The computer tries to guess the number that the user is thinking of

print("Think of a number between 1 and 100, and I will try to guess it!")

low = 1        # lower bound of the search range
high = 100     # upper bound of the search range

while True:
    # The computer guesses the middle of the current range
    guess = (low + high) // 2
    print(f"My guess is: {guess}")

    # Ask the user for feedback
    answer = input("Is your number higher (>), lower (<), or correct (=)? ")

    if answer == "=":
        # If the guess is correct, stop the loop
        print("Yay! I guessed your number!")
        break

    elif answer == ">":
        # If the number is higher, update the lower bound
        low = guess + 1

    elif answer == "<":
        # If the number is lower, update the upper bound
        high = guess - 1

    else:
        # Handle invalid input
        print("Please enter only >, <, or =")