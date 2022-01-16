'''
Calculate the number of expected green and yellow 
tiles for a Wordle starting word, given a list of 
allowable guesses and a list of possible answers.
'''
# DataFrames, arrays
import pandas as pd
import numpy as np

# Progress bar
from tqdm import tqdm


# Paths to allowed guesses, possible answers, and output CSV files
GUESSES_CSV = 'PATH/TO/GUESSES.CSV'
ANSWERS_CSV = 'PATH/TO/ANSWERS.CSV'
OUT_CSV = 'OUT/PATH.CSV'


def score_guess(guess: str, word: str):
    '''
    Count the number of green and yellow tiles 
    a guessed word would yield on a Wordle word.
    '''
    assert len(guess) == 5 and len(word) == 5, \
        "One of the words provided is not five letters!"

    green_tiles = 0
    matched_indices = []
    for i, char in enumerate(guess):
        # Add to green if characters match at same position, 
        # record indices where green tiles happened
        if char == word[i]:
            green_tiles += 1
            matched_indices.append(i)
        else:
            pass
    
    def remove_char(words: list, indices: list) -> list:
        '''
        Remove characters at a specific index 
        from a list of multiple strings.
        '''
        new_words = []
        for word in words:
            new_words.append(''.join([word[i] for i in range(len(word)) if i not in indices]))
        return new_words

    remaining_chars = remove_char([guess, word], matched_indices)
    guess_chars = remaining_chars[0]
    word_chars = remaining_chars[1]

    yellow_tiles = 0
    if len(guess_chars) != 0:
        for i, char in enumerate(guess_chars):
            # If the guess has a character in the remaining characters
            # of the word, then increment yellow_tiles and remove the
            # character from the word.
            if char in word_chars:
                yellow_tiles += 1
                word_chars = remove_char([word_chars], [word_chars.index(char)])[0]
            else:
                pass
                
    return green_tiles, yellow_tiles


if __name__ == '__main__':
    # Read in word lists, make arrays
    guess_df = pd.read_csv(GUESSES_CSV)
    guesses = np.asarray(guess_df)
    answers = np.asarray(pd.read_csv(ANSWERS_CSV))

    # Initialize scoring arrays
    green_scores = np.zeros(guesses.shape)
    yellow_scores = np.zeros(guesses.shape)

    # Compare all allowed guesses with possible answers pairwise, 
    # summing green and yellow tiles and storing in arrays
    for i, guess in enumerate(tqdm(guesses)):
        green_score = 0
        yellow_score = 0

        for answer in answers:
            green, yellow = score_guess(guess[0], answer[0])
            green_score += green
            yellow_score += yellow
        
        green_scores[i] = green_score
        yellow_scores[i] = yellow_score
    
    # Divide by number of answers for expected values
    green_scores /= answers.shape[0]
    yellow_scores /= answers.shape[0]

    # Put into DF and save
    guess_df['green_expected'] = green_scores
    guess_df['yellow_expected'] = yellow_scores
    guess_df.to_csv(OUT_CSV, index=False)

