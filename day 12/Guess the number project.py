import random

def choose_difficulty(difficulty):
    if difficulty == "easy":
        player_lives = 5
        return player_lives
    elif difficulty == "hard":
        player_lives = 10
        return player_lives


def player_guess_correct(guess):
    if guess == random_number:
        return True
    else:
        return False

guess_list = []
player_lives = 0
difficulty_modifier_aka_lives = int(choose_difficulty(input("Choose Diff easy or hard? ")))
random_number = random.randint(1,100)
print(random_number)





while len(guess_list) < difficulty_modifier_aka_lives:
    player_guess = int(input("What's Your Guess? "))
    if player_guess_correct(player_guess) == True:
        print("You're A Wizard Harry.")
        break
    else:
        if player_guess > random_number:
            guess_list.append(player_guess)
            print(guess_list)
            n = len(guess_list)
            if difficulty_modifier_aka_lives - n == 0:
                print(f"YOU LOST. GGWP")
            else:
                print(f"Guess Again you have {difficulty_modifier_aka_lives - n} lives remaining. Also, Lower")
        elif player_guess < random_number:
            guess_list.append(player_guess)
            print(guess_list)
            n = len(guess_list)
            if difficulty_modifier_aka_lives - n == 0:
                print(f"YOU LOST. GGWP")
            else:
                print(f"Guess Again you have {difficulty_modifier_aka_lives - n} lives remaining. Also, Higher ")
        

    
    











