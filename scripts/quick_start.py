import time
import imageio
import gymnasium as gym
import numpy as np

import gym_hil

# Use the Franka environment
env = gym.make("gym_hil/PandaPickCubeBase-v0", render_mode="human", image_obs=True)
action_spec = env.action_space

obs, info = env.reset()
frames = []

for i in range(200):
    obs, rew, done, truncated, info = env.step(env.action_space.sample())
    # info contains the key "is_intervention" (boolean) indicating if a human intervention occurred
    # If info["is_intervention"] is True, then info["action_intervention"] contains the action that was executed
    images = obs["pixels"]
    frames.append(np.concatenate((images["front"], images["wrist"]), axis=0))

    if done:
        obs, info = env.reset()

env.close()
imageio.mimsave("franka_render_test.mp4", frames, fps=20)