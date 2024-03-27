import tkinter as tk
from typing import Optional, Union, List

import gym
from gym import spaces
import numpy as np
from gym.core import RenderFrame

from rule import check_winner
class FiveChessGameEnv(gym.Env):
    def __init__(self, master):
        super(FiveChessGameEnv, self).__init__()
        self.master = master
        self.master.title("五子棋")
        self.board_size = 14
        self.canvas = tk.Canvas(master, width=450, height=450, bg="white")
        self.canvas.pack()
        self.observation_space = spaces.Box(low=0, high=2, shape=(self.board_size, self.board_size),dtype=np.float32)
        self.action_space = spaces.MultiBinary(self.board_size * self.board_size)
        self.current_winner = None
        self.current_player = None
        self.board = None
        self.draw_board()


        self.error_label = tk.Label(master, text="", fg="red")
        self.error_label.pack()
        self.canvas.bind("<Button-1>", self.on_click)

        self.exit_button = tk.Button(master, text="退出", command=self.exit_program)
        self.exit_button.pack()

        self.undo_onestep = tk.Button(master, text="悔棋一步", command=self.undo_onestep)
        self.undo_onestep.pack()
        self.reset()

    def reset(self):
        self.current_player = 1
        #初始化棋盘，全0代表located space
        self.board = np.zeros((self.board_size, self.board_size), dtype=np.float32)
        self.current_winner = 'None'
        self.draw_board()
        return self.board

    def step(self, action):
        row,col = action
        action_reward = self.click_judge(row,col)
        if action_reward == -1:
            return self.board.copy(),-1,True,{'error':True,'message':'Invalid action'}
        elif action_reward >= 5:
            reward = 1
            done = True
        elif action_reward == 4:
            reward = 0.1
            done = False
        else :
            reward = 0
            done = False
        next_observation = self.board.copy()
        return next_observation, reward, done,{}


    def draw_board(self):
        for i in range(15):
            self.canvas.create_line(30, 30 * i + 30, 450 - 30, 30 * i + 30)
            self.canvas.create_line(30 * i + 30, 30, 30 * i + 30, 450 - 30)


    def on_click(self, event):
        x, y = event.x, event.y
        col = round((x - 15) / 30)
        row = round((y - 15) / 30)
        if not (0 < row < 14 and 0 < col < 14):
            self.error_label.config(text="错误：超出棋盘范围！")
            return -1
        else:
            self.click_judge(col, row)


    def click_judge(self,col,row):
        if self.board[row][col] == 0:

            place_color = 1 if self.current_player == 1 else 2
            self.current_player = 2 if self.current_player == 1 else 1

            piece = self.canvas.create_oval(col * 30 + 15 - 13, row * 30 + 15 - 13, col * 30 + 15 + 13,
                                            row * 30 + 15 + 13,
                                            fill="black" if place_color == 1 else "white")
            self.board[row][col] = place_color
            return check_winner(self.board, place_color,row,col)
            # if check_winner(self.board, place_color,row,col) >= 5:
            #     self.error_label.config(text=f"恭喜 {place_color} 玩家获胜！")
            #     self.current_winner = place_color
            #     # self.canvas.unbind("<Button-1>")
            # else:
            #     self.error_label.config(text="")
        else:
            self.error_label.config(text="错误：该位置已经有棋子了")
            return -1

    def undo_onestep(self):
        history,place_color,pre_row,pre_col = self.board
        self.canvas.delete(history)
        self.current_player = 1 if self.current_player == 2 else 1

    def exit_program(self):
        self.master.destroy()

