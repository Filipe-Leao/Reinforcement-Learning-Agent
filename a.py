import gymnasium as gym
import time
import ale_py
import pygame

gym.register_envs(ale_py)

env = gym.make("ALE/MsPacman-v5", render_mode="human")
obs, info = env.reset()

done = False
while not done:
    obs, reward, terminated, truncated, info = env.step(env.action_space.sample())
    done = terminated or truncated

env.close()
