import numpy as np
import time
import random
import gym
import matplotlib.pyplot as plt

env = gym.make("FrozenLake-v0")

action_size = env.action_space.n
state_size = env.observation_space.n

qtable = np.zeros((state_size, action_size))

learning_rate = 0.8
max_steps = 99
gamma = 0.95

epsilon = 1.0
max_epsilon = 1.0
min_epsilon = 0.01
decay_rate = 0.005

rewards = []
steps_by_total_episodes = []
rate_by_total_episodes = []

total_episodes = 30000
delta_episodes = 1000

for episode in range(1, total_episodes+1):
    state = env.reset()
    step = 0
    done = False
    total_rewards = 0
    
    for step in range(max_steps):
        exp_exp_tradeoff = random.uniform(0, 1)

        if exp_exp_tradeoff > epsilon:
            action = np.argmax(qtable[state,:])

        else:
            action = env.action_space.sample()

        new_state, reward, done, info = env.step(action)

        # Update Q(s,a)
        qtable[state, action] = qtable[state, action] + learning_rate * (reward + gamma * np.max(qtable[new_state, :]) - qtable[state, action])

        total_rewards += reward

        state = new_state

        if done == True:
            break
  
  # epsilon_decay
    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)
    rewards.append(total_rewards)
    
    if episode % delta_episodes == 0: 
        success_cnt = 0
        step_sum = 0

        for episode in range(1000):
            state = env.reset()
            step = 0
            done = False

            for step in range(max_steps):
                action = np.argmax(qtable[state, :])
                new_state, reward, done, info = env.step(action)
        
                if done:
                    print(info)
                    if step != max_steps - 1:
                        success_cnt += 1
                        step_sum += 1
                    
                    break

                state = new_state

        average = step_sum / success_cnt
        rate = success_cnt / 1000

        steps_by_total_episodes.append(average)
        rate_by_total_episodes.append(rate)

plt.subplot(2,1,1)
plt.plot(range(delta_episodes, total_episodes + 1, delta_episodes), steps_by_total_episodes, color='red')
plt.xlabel('episodes')
plt.ylabel('steps')

plt.subplot(2,1,2)
plt.plot(range(delta_episodes, total_episodes + 1, delta_episodes), rate_by_total_episodes, color='blue')
plt.xlabel('episodes')
plt.ylabel('rate')

plt.show()
env.close()
