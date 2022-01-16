# wordle
Scripts for Wordle, a game about guessing a five-letter word: https://www.powerlanguage.co.uk/wordle/

## Dependencies
`numpy`, `pandas`, `tqdm`

## Code
expected_green_yellow_guess.py: Given a CSV file of allowed guesses and possible answers, calculate the average number of green and yellow tiles a guess yields on the possible answers. The algorithm scores a guess against all possible answers, and:

1. finds letter and position matches between the two words and increments the green-tile counter,
2. removes these green letters from both the guess and the answer,
3. for each remaining letter in the guess, checks to see if it is in the remaining letters of the answer, incrementing the yellow-tile counter if so,
4. removes this letter from both the guess and the answer,
5. divides the green and yellow counters by the number of possible answers

to yield the expected number of green and yellow tiles of a guess.


rank_wordle.py: Ranks best and worst words, according so schemes where green tiles are worth n times the point-value of yellow tiles.

## Outputs
expected_green_yellow.csv is the output of expected_green_yellow_guess.py, if ran on wordle-allowed-guesses.csv and wordle-answers-alphabetical.csv.

weighted_scores.csv is the output of rank_wordle.py, if ran on expected_green_yellow.csv.
