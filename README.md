# Malayalam Movie Guessing Game  

## Project Overview  
This is a fun command-line game built with **Python** and **Pandas**, where players try to guess the name of a Malayalam movie based on clues like:  
- Director  
- Main Cast  
- Movie Plot  

The game selects a random movie from a dataset (`malayalam_movies.csv`) and gives you clues one by one. Your score depends on how quickly you guess the movie!  

---

## Features  
- Random movie selection from dataset  
- Multiple clues per movie (Director, Cast, Summary)  
- Scoring system (higher points for fewer attempts)  
- Keeps track of total score across rounds  
- Option to play multiple rounds  

---

## Dataset Format (`malayalam_movies.csv`)  
The dataset should have the following columns:  

| Movie Name | Director | Cast | Summary |  
|------------|----------|------|---------|  
| Drishyam   | Jeethu Joseph | Mohanlal, Meena, Asha Sarath | A man goes to great lengths to protect his family after a crime. |  
| Premam     | Alphonse Puthren | Nivin Pauly, Sai Pallavi, Madonna Sebastian | A coming-of-age romantic drama following George’s journey through love and life. |  

---

## How to Play  
1. Clone or download this repository.  
2. Make sure you have Python 3 installed.  
3. Install Pandas if not already installed:
  ```bash
   pip install pandas
```
4. Place the dataset malayalam_movies.csv in the project folder.
5. Run the game
   ```bash
   python MOVIE_GAME.py
6. Follow the clues and try to guess the movie!



# Scoring System  

- You start each round with **maximum points** (equal to the number of clues).  
- Each wrong attempt deducts **1 point**.  
- If you fail to guess after all clues, you score **0** for that round.  
- Your total score accumulates across rounds.  

---

# Future Improvements  

- Add genre as a clue  
- Add difficulty levels (easy/medium/hard)  
- Create a leaderboard system  
- Build a simple GUI version  
