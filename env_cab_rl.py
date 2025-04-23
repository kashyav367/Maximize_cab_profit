# env_cab_rl.py

import gym
from gym import spaces
import numpy as np

class CabEnvRL(gym.Env):
    def __init__(self, features, rewards):
        super(CabEnvRL, self).__init__()
        self.features = features.values
        self.rewards = rewards.values
        self.n_samples = len(self.features)
        self.current_index = 0

        self.observation_space = spaces.Box(low=0, high=1, shape=(self.features.shape[1],), dtype=np.float32)
        self.action_space = spaces.Discrete(2)  # 0: Reject, 1: Accept

    def reset(self):
        self.current_index = np.random.randint(0, self.n_samples)
        return self.features[self.current_index]

    def step(self, action):
        reward = 0
        done = True

        if action == 1:  # Accept ride
            reward = self.rewards[self.current_index]
        else:  # Reject ride
            reward = -1

        next_state = self.reset()
        return next_state, reward, done, {}
