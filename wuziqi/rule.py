import tkinter as tk
def check_winner(board, color,row,col):
    # 检查水平方向

    max_count = max(check_direction(board,color, row, col, 1, -1),
           check_direction(board, color, row, col, 1, 1),
           check_direction(board, color, row, col, 1, 0),
           check_direction(board, color, row, col, 0, 1))
    print(max_count)
    return max_count

def check_direction(board, color, row, col, dr, dc):
    count = 1

    # 向指定方向移动，直到遇到不同颜色的棋子或者到达边界
    r, c = row + dr, col + dc
    while 0 < r < 14 and 0 < c < 14 and (board[r][c] == color):
        count += 1
        r += dr
        c += dc
    # 反方向移动，直到遇到不同颜色的棋子或者到达边界
    r, c = row - dr, col - dc
    while 0 < r < 14 and 0 < c < 14 and (board[r][c] == color):
        count += 1
        r -= dr
        c -= dc

    # 如果达到了五个相同颜色的棋子，则返回 True，表示胜利
    return count