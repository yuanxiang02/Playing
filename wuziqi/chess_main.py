import tkinter as tk
from board_chess import FiveChessGameEnv
import numpy as np
import matplotlib.pyplot as plt
import gym
from torch.utils.tensorboard import SummaryWriter
import torch
from PPO_trainer import PPO



device = torch.device('cuda:2') if torch.cuda.is_available() \
                            else torch.device('cpu')
board_size = 14
num_episodes = 80  # 总迭代次数
num_epochs = 15
gamma = 0.9  # 折扣因子
actor_lr = 1e-3  # 策略网络的学习率
critic_lr = 1e-2  # 价值网络的学习率
n_hiddens = 16  # 隐含层神经元个数
lmbda_item = 0.95
eps_date = 0.2
env_name = 'FiveChessGameEnv'
# ----------------------------------------- #
# 环境加载
# ----------------------------------------- #

def main():
    # writer = SummaryWriter('logs')             writer.add_scalar('Training/Loss', loss, global_step=i)
    env = FiveChessGameEnv()
    agent = PPO(
        n_states = board_size * board_size,
        n_hiddens = n_hiddens,
        n_actions = board_size * board_size,
        actor_lr = actor_lr,
        critic_lr = critic_lr,
        lmbda = lmbda_item,
        epochs = num_epochs,
        eps = eps_date,
        gamma = gamma,
        device = device
    )

    for i in range(num_episodes):
        obs = env.reset()
        done = False
        total_reward = 0
        transition_dict = {
            'states': [],
            'actions': [],
            'next_states': [],
            'rewards': [],
            'dones': [],
        }

        while not done :
            action,log_prob = agent.take_action(obs,board_size)
            # summary_Writer(log_prob)
            next_obs,reward,done = env.step(action)
            transition_dict['states'].append(obs)
            transition_dict['actions'].append(action)
            transition_dict['next_states'].append(next_obs)
            transition_dict['rewards'].append(reward)
            transition_dict['dones'].append(done)
            obs = next_obs
            total_reward += reward
        agent.learn(transition_dict)


    # root = tk.Tk()
    # game = FiveChessGameEnv(root)
    # root.mainloop()


if __name__ == "__main__":
    main()