import gymnasium as gym
import ale_py

gym.register_envs(ale_py)

env = gym.make("ALE/MsPacman-v5", render_mode="human")

observation, info = env.reset()
done = False
while not done:
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated

env.close()
