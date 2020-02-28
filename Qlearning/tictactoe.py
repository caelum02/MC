#%%
!python gymtictactoe/setup.py install

#%%
import gym
import numpy
import gym_tictactoe

#%%
env = gym.make('TicTacToe-v1')  
env.init(symbols=[-1, 1]) # Define users symbols
user 
done = False
reward = 0

# Reset the env before playing
state = env.reset()

while not done:
    env.render(mode=None)
    if user == 0:
        state, reward, done, infos = env.step(env.action_space.sample(), -1)
    elif user == 1:
        state, reward, done, infos = env.step(env.action_space.sample(), 1)
       
    # If the game isn't over, change the current player
    if not done:
        user = 0 if user == 1 else 1
    else :
        if reward == 10:
            print("Draw !")
        elif reward == -20:
            print("Infos : " + str(infos))
            if user == 0:
                print("Random wins ! AI Reward : " + str(reward))
            elif user == 1:
                print("AI wins ! AI Reward : " + str(-reward))
        elif reward == 20:
            if user == 0:
                print("AI wins ! AI Reward : " + str(reward))
            elif user == 1:
                print("Random wins ! AI Reward : " + str(reward))

#%%
