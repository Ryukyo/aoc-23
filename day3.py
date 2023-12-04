import math
import re

board = list(open('day3.txt'))
# 140 chars per line
chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}

for pos, row in enumerate(board):
    for match in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (pos - 1, pos, pos + 1)
                       for c in range(match.start() - 1, match.end() + 1)}

        for t_row_char in edge & chars.keys():
            chars[t_row_char].append(int(match.group()))

print(sum(sum(p)    for p in chars.values()))