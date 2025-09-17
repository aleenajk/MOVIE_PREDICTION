import pandas as pd
import random

df = pd.read_csv('malayalam_movies.csv', low_memory=False)

def play_game():
    print("Welcome to Guess the Movie Game!\n")
    play_again = 'y'
    total_score = 0  

    while play_again.lower() == 'y':
        movie = df.sample(1).iloc[0]
        clues = {
            "Main Cast": movie['Cast'],
            "Movie plot":movie['Summary'],
            "Director": movie['Director'],
            
        }
        attempts = 0
        max_attempts = len(clues)
        round_score = max_attempts  # Start round with max points

        print("Try to guess the movie!")
        for clue_name, clue_value in clues.items():
            print(f"\nClue ({attempts+1}/{max_attempts}): {clue_name} → {clue_value}")
            guess = input("Your guess: ")
            attempts += 1

            if guess.strip().lower() == movie['Movie Name'].strip().lower():
                print(f"\nCorrect! You guessed it in {attempts} attempt(s).")
                print(f"You scored {round_score} point(s) this round.")
                total_score += round_score
                break
            else:
                round_score -= 1 
        else:
            print(f"\nOut of clues! The movie was: {movie['Movie Name']}")
            print("You scored 0 points this round.")

        print(f"Total Score: {total_score}")
        # Ask to play again
        play_again = input("\nDo you want to play again? (y/n): ")
        print("-" * 50)

if __name__ == "__main__":
    play_game()
