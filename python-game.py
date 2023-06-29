def check_answer(question, answer):
    # Function to check if the user's guess matches the answer
    guess = input(question + " ")
    return guess.lower() == answer.lower()

def play_game():
    # Game logic
    score = 0
    guesses_remaining = 3

    # Question 1
    if check_answer("What is the capital of France?", "Paris"):
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        guesses_remaining -= 1

    # Question 2
    if check_answer("Which planet is known as the Red Planet?", "Mars"):
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        guesses_remaining -= 1

    # Question 3
    if check_answer("What is the largest continent?", "Asia"):
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        guesses_remaining -= 1

    # Final score
    print("Game over!")
    print("Your score: " + str(score) + "/3")

    if score == 3:
        print("Congratulations! You answered all questions correctly.")
    else:
        print("Better luck next time!")

    if guesses_remaining == 0:
        print("You have used all your guesses.")

play_game()
