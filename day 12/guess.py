from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

logo = """
  ______                                          __                                                                       
 /      \                                        /  |                                                                      
/$$$$$$  | __    __   ______    _______  _______ $$/  _______    ______          ______    ______   _____  ____    ______  
$$ | _$$/ /  |  /  | /      \  /       |/       |/  |/       \  /      \        /      \  /      \ /     \/    \  /      \ 
$$ |/    |$$ |  $$ |/$$$$$$  |/$$$$$$$//$$$$$$$/ $$ |$$$$$$$  |/$$$$$$  |      /$$$$$$  | $$$$$$  |$$$$$$ $$$$  |/$$$$$$  |
$$ |$$$$ |$$ |  $$ |$$    $$ |$$      \$$      \ $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ | /    $$ |$$ | $$ | $$ |$$    $$ |
$$ \__$$ |$$ \__$$ |$$$$$$$$/  $$$$$$  |$$$$$$  |$$ |$$ |  $$ |$$ \__$$ |      $$ \__$$ |/$$$$$$$ |$$ | $$ | $$ |$$$$$$$$/ 
$$    $$/ $$    $$/ $$       |/     $$//     $$/ $$ |$$ |  $$ |$$    $$ |      $$    $$ |$$    $$ |$$ | $$ | $$ |$$       |
 $$$$$$/   $$$$$$/   $$$$$$$/ $$$$$$$/ $$$$$$$/  $$/ $$/   $$/  $$$$$$$ |       $$$$$$$ | $$$$$$$/ $$/  $$/  $$/  $$$$$$$/ 
                                                               /  \__$$ |      /  \__$$ |                                  
                                                               $$    $$/       $$    $$/                                   
                                                                $$$$$$/         $$$$$$/                                    """
print(logo)


def check_answer(guess, answer, turns):
    """Checks answer against guest guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You  got it! The answer was {answer}.")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number Guessing Game!.")
    print("I'm thinking of a number to guess between 1 and 100.")

    answer = randint(1, 100)
    print(f"psst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again")


game()


