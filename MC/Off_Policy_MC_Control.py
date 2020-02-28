from EnvRacetrack import Racetrack
import numpy as np
import random
import statistics

track1 = np.loadtxt('track1')

Q = np.random.rand(32, 17, 5, 5, 9) #[i,j,vi,vj,a]
C = np.zeros_like(Q)
P = np.argmax(Q, axis=4)

env = Racetrack(track1)

GAMMA = 1
EPISODES_TO_EXPLORE = 10000

learnLog = []

for it in range(0, 100):
    for i in range(0, 0000):
        AQ = []
        SQ = []
        RQ = []
   
        state = env.reset()
        done = False

        SQ.append(state)

        while not done:
            action = random.choice(env.possibleActs())
            rwd, state, done = env.step(action)

            AQ.append(action)
            RQ.append(rwd)
            SQ.append(state)

        T = len(AQ)
        print('Episode %d Done with %d states' %(i, T))

        G = 0
        W = 1

        for t in range(T-1, -1, -1):
            G += GAMMA * RQ[t]

            C[SQ[t][0]][SQ[t][1]][SQ[t][2]][SQ[t][3]][AQ[t]] += W
            Q[SQ[t][0]][SQ[t][1]][SQ[t][2]][SQ[t][3]][AQ[t]] += W / C[SQ[t][0]][SQ[t][1]][SQ[t][2]][SQ[t][3]][AQ[t]] * (G - Q[SQ[t][0]][SQ[t][1]][SQ[t][2]][SQ[t][3]][AQ[t]])
            P[SQ[t][0]][SQ[t][1]][SQ[t][2]][SQ[t][3]] = np.argmax(Q[SQ[t][0]][SQ[t][1]][SQ[t][2]][SQ[t][3]])

            if AQ[t] != P[SQ[t][0]][SQ[t][1]][SQ[t][2]][SQ[t][3]]:
                break

            W *= 1 / (1 / len(env.possibleActs()))
    
    print('Evaluating...')
    rwds = 0 
    for i in range(0, 20):
        state = env.reset()
        done = False
        rwd = 0
        SQ.append(state)

        while not done:
            action = P[state[0]][state[1]][state[2]][state[3]]
            rwd, state, done = env.step(action)

        print('Exploitation %d done' %i)
        rwds += rwd

    print('iteration %d with score %d' %(it, rwds / 20))
    learnLog.append(np.mean(rwds))

np.savetxt('learnLog', np.array(learnLog))