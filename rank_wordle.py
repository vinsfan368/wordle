'''
Given expected green and yellow scores for every 
guess, rank them in some arbitrary order based on 
the relative value of green and yellow tiles.
'''
# DataFrames, arrays
import pandas as pd
import numpy as np


# Column names for green and yellow expected scores
WORD_COL = 'guesses'
GREEN_COL = 'green_expected'
YELLOW_COL = 'yellow_expected'

# Expected values CSV file and output CSV
EXPECT_VALUES = 'PATH/TO/EXPECTED/VALUES.CSV'
OUT_CSV = 'OUT/PATH.CSV'


if __name__ == '__main__':
    score_df = pd.read_csv(EXPECT_VALUES)
    words = np.asarray(score_df[WORD_COL])
    green = np.asarray(score_df[GREEN_COL])
    yellow = np.asarray(score_df[YELLOW_COL])

    # Calculate scores, where green is worth some multiple of yellow
    green2 = (green * 2) + yellow
    green3 = (green * 3) + yellow
    green4 = (green * 4) + yellow
    green5 = (green * 5) + yellow

    green2_top10 = words[np.argsort(green2)[:-10:-1]]
    green3_top10 = words[np.argsort(green3)[:-10:-1]]
    green4_top10 = words[np.argsort(green4)[:-10:-1]]
    green5_top10 = words[np.argsort(green5)[:-10:-1]]

    print(f'The 10 highest scoring words where a green tile is worth twice a yellow tile are {green2_top10}')
    print(f'The 10 highest scoring words where a green tile is worth three times a yellow tile are {green3_top10}')
    print(f'The 10 highest scoring words where a green tile is worth four times a yellow tile are {green4_top10}')
    print(f'The 10 highest scoring words where a green tile is worth five times a yellow tile are {green5_top10}')

    green2_bot10 = words[np.argsort(green2)[:10]]
    green3_bot10 = words[np.argsort(green3)[:10]]
    green4_bot10 = words[np.argsort(green4)[:10]]
    green5_bot10 = words[np.argsort(green5)[:10]]

    print(f'The 10 lowest scoring words where a green tile is worth twice a yellow tile are {green2_bot10}')
    print(f'The 10 lowest scoring words where a green tile is worth three times a yellow tile are {green3_bot10}')
    print(f'The 10 lowest scoring words where a green tile is worth four times a yellow tile are {green4_bot10}')
    print(f'The 10 lowest scoring words where a green tile is worth five times a yellow tile are {green5_bot10}')
    
    score_df['green2'] = green2
    score_df['green3'] = green3
    score_df['green4'] = green4
    score_df['green5'] = green5

    score_df.to_csv(OUT_CSV)