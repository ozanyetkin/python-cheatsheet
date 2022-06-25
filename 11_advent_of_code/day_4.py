from matplotlib.pyplot import draw
import pandas as pd
import numpy as np

drawn_numbers = [59,91,13,82,8,32,74,96,55,51,19,47,46,44,5,21,95,71,48,60,68,81,80,14,23,28,26,78,12,22,49,1,83,88,39,53,84,37,93,24,42,7,56,20,92,90,25,36,34,52,27,50,85,75,89,63,33,4,66,17,98,57,3,9,54,0,94,29,79,61,45,86,16,30,77,76,6,38,70,62,72,43,69,35,18,97,73,41,40,64,67,31,58,11,15,87,65,2,10,99]

df = pd.read_table("./11_advent_of_code/day_4.txt", header=None, delim_whitespace=True)
bingo_boards = np.array(df, dtype=object)

def checker(board):
    for i in range(5):
        count_r = 0
        count_c = 0
        for j in range(5):
            if board[i][j] == "X":
                count_r += 1
            if board[j][i] == "X":
                count_c += 1
        if count_c == 5 or count_r == 5:
            return "WIN"

def unmark_sum(board):
    sum = 0
    for i in range(5):
        for j in range(5):
            try:
                sum += board[i][j]
            except:
                pass
    return sum

def play():
    for drawn in drawn_numbers:
        bingo_boards[bingo_boards == drawn] = "X"
        for i in range(0, 500, 5):
            if checker(bingo_boards[i:i+5, 0:]) == "WIN":
                return unmark_sum(bingo_boards[i:i+5, 0:]) * drawn


def lose():
    winners = []
    aday = list(range(100))
    for drawn in drawn_numbers:
        bingo_boards[bingo_boards == drawn] = "X"
        aday_new = []
        for i in [a * 5 for a in aday]:
            if checker(bingo_boards[i:i+5, 0:]) == "WIN":
                winners.append((unmark_sum(bingo_boards[i:i+5, 0:]) * drawn))
            else:
                aday_new.append(int(i/5))
        aday = aday_new
    return winners[-1]

print(play())
print(lose())