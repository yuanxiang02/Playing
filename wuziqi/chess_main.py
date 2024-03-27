import tkinter as tk
from board_chess import FiveChessGameEnv
import numpy as np
import matplotlib.pyplot as plt
import gym
import torch
from PPO_trainer import PPO



device = torch.device('cuda') if torch.cuda.is_available() \
                            else torch.device('cpu')

num_episodes = 100  # 总迭代次数
gamma = 0.9  # 折扣因子
actor_lr = 1e-3  # 策略网络的学习率
critic_lr = 1e-2  # 价值网络的学习率
n_hiddens = 16  # 隐含层神经元个数
env_name = 'wuzi_chess'
return_list = []  # 保存每个回合的return

# ----------------------------------------- #
# 环境加载
# ----------------------------------------- #

# env = gym.make(env_name, render_mode="human")
# n_states = env.observation_space.shape[0]  # 状态数 4
# n_actions = env.action_space.n  # 动作数 2


def main():
    root = tk.Tk()
    game = FiveChessGameEnv(root)
    root.mainloop()


if __name__ == "__main__":
    main()