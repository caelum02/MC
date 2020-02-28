#%%
import game
import numpy as np
import copy

env = game.env()

old_agent = game.agent()

#%%
for i in range(1):
    new_agent = copy.deepcopy(old_agent)

    for episode in range(10000):
        if (episode + 1) %200 == 0:
            print('%d episodes played' %(episode))
        step = 0
        done = False
        player = 1 # 1 : new, -1 : old

        agent = [new_agent, old_agent]
        state = env.reset()     

        action = agent[step%2].get_action(state)
        new_state, reward, done = env.step(action, player)

        step += 1
        player *= -1

        bef_action = action
        bef_state = state
        bef_reward = reward

        state = new_state

        while not done:
            action = agent[step%2].get_action(player*state)
            new_state, reward, done = env.step(action, player)       

            agent[(step+1)%2].learn(bef_state, bef_action, new_state, bef_reward-reward)
            if done or step==8:
                agent[step%2].learn(state, action, new_state, reward)
                break

            bef_action = action
            bef_state = state
            bef_reward = reward

            state = new_state

            step += 1
            player *= -1
#%%
def actcompress(i, j):
    return 3*i+j

#%%
state = env.reset()
agent = old_agent
step = 0
done = False
while not done:
    print(step)
    if step % 2==0:
        action = agent.get_action(state)
    else:
        acti, actj = input().split()
        action = actcompress(int(acti), int(actj))

    new_state, reward, done = env.step(action, player)       
    env.render()

    if done or step==8:
        break

    state = new_state

    step += 1
    player *= -1


#%%
