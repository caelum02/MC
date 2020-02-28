import numpy as np

class Racetrack:
    def __init__(self, track):
        self.track = track
        self._state = None

    def reset(self):
        si, sj =  np.where(self.track==1)
        randIdx = np.random.randint(len(si))
        
        self._state = [si[randIdx], sj[randIdx], 0, 0]

        return self._state

    def _actMap(self, actionIdx):
        # actionIdx : 0~9

        return [actionIdx//3 - 1, actionIdx%3 - 1]

    def step(self, actionIdx):
        action = self._actMap(actionIdx)

        self._state[2] += action[0]
        self._state[3] += action[1]

        nxtState = self._state[:2]
        nxtState[0] += self._state[2]
        nxtState[1] += self._state[3]

        rwd = 0
        done = False

        if self.track[nxtState[0]][nxtState[1]] == 2:
            done = True

        elif self.track[nxtState[0]][nxtState[1]] == -1:
            self._state = self.reset()
            rwd = -2

        else:
            self._state[:2] = nxtState
            rwd = -1

        return rwd, self._state, done
    
    def possibleActs(self):
        # Only velocity in 0~4 available
        
        flags = [1 for _ in range(9)]

        st = self._state
        if st[2]==0:
            for i in [0,1,2]:
                flags[i] = 0

        if st[2]==4:
            for i in [6,7,8]:
                flags[i] = 0

        if st[3]==0:
            for i in [0,3,6]:
                flags[i] = 0

        if st[3]==4:
            for i in [2,5,8]:
                flags[i] = 0

        acts = [] 
        for i, flag in enumerate(flags):
            if flag: acts.append(i)

        return acts

if __name__=='__main__':
    env = Racetrack(track1)
    print(track1)