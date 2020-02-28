import numpy as np
import random

def state_encoder(state):
    flat = state.flatten() + 1
    basis = np.array([3**i for i in range(9)])

    return int(np.dot(flat, basis))

class agent:
    def __init__(self):
        self.epsilon = 1
        self.decay = 0.00001
        self.qtable = np.zeros((3 ** 9, 9))
        self.lr = 0.8
        self.gamma = 0.9

        self.eps_min = 0.3


    def get_action(self, state):
        encstate = state_encoder(state)

        self.epsilon = self.eps_min + (self.epsilon-self.eps_min) * np.exp(-self.decay)

        if random.uniform(0, 1) < self.epsilon:
            while True:
                randact = random.randint(0, 8)

                if state[randact//3][randact%3]==0:
                    return randact
    
        else:
            q = self.qtable[encstate,:].copy()
            while True:
                act = np.argmax(q)
                if state[act//3][act%3]!=0:
                    q[act] -= 99999999 
                else:
                    return act
        

    def learn(self, state, action, new_state, reward):
        new_state = state_encoder(new_state)
        state = state_encoder(state)

        delta = reward + self.gamma * np.max(self.qtable[new_state, :]) - self.qtable[state][action]
        self.qtable[state, action] += self.lr * delta


class env:
    def __init__(self):
        self.state = np.zeros([3, 3])

    def isDone(self):
        for i in range(3):
            if self.state[i][0]!=0 and self.state[i][0]==self.state[i][1] and self.state[i][1]==self.state[i][2]:
                return True
            if self.state[0][i]!=0 and self.state[0][i]==self.state[1][i] and self.state[1][i]==self.state[2][i] and self.state[0][i]!=0:
                return True
        
        if self.state[0][0]!=0 and self.state[0][0]==self.state[1][1] and self.state[1][1]==self.state[2][2]:
            return True
            
        if self.state[2][0]!=0 and self.state[2][0]==self.state[1][1] and self.state[1][1]==self.state[0][2]:
            return True
        
        return False


    def step(self, action, player):
        '''
        return new_state, reward, done, error
        '''
        act_i, act_j = action // 3, action % 3
        # print('(%d, %d), player : %d' %(act_i, act_j, player))

        if self.state[act_i][act_j] != 0:
            return np.zeros([3, 3]), -1, True

        self.state[act_i][act_j] = player

        if self.isDone():
            return np.zeros([3, 3]), 1, True

        return self.state, 0, False

    def reset(self):
        self.state = np.zeros([3, 3], dtype=np.int32)

        return self.state

    def render(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j]==1:
                    print("O", end='')
                elif self.state[i][j]==0:
                    print("*", end='')
                else:
                    print("X", end='')
            print()
        
        print()


