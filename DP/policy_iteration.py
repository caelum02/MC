import numpy as np
import math
import itertools

MAX_CAR = 20
MAX_MOV = 5
E_REQ_1 = 3 
E_REQ_2 = 4
E_RET_1 = 3
E_RET_2 = 2
GAMMA = 0.9


V = np.random.random((MAX_CAR+1, MAX_CAR+1))
policy_stable = False
theta = 0.1
pi = np.zeros((MAX_CAR+1, MAX_CAR+1))

while not policy_stable:
    delta = theta 
   
    while delta >= theta:
        delta = 0
        v = V
        V = 0
        delta = np.max(delta, np.abs(v-V))

    policy_stable = True
    old_action = pi.copy()
    policy_stable = np.array_eqaul()



