#!/bin/python3

import gym

def findBall(observation):
    for x in range(34, 194): # board starts at row 34 and ends at row 160
        for y in range(len(observation[0])):
            t = True
            for i in range(3):
                t &= (observation[x][y][i] > 200) # ball is color 236,236,236
            if t:
                return x+1
    return 114


def findPlayer(observation):
    for x in range(34, 194):
        for y in range(len(observation[0])):
            # player in color 92,186,92
            if observation[x][y][0]==92 and observation[x][y][1]==186 and observation[x][y][2]==92:
                return x+7
    return 0


env = gym.make('Pong-v0')
o = env.reset()
done = False
c = False
while not done:
    env.render()
    # crazy ai logic here
    b = findBall(o)
    p = findPlayer(o)
    action = 0
    if c:
        if b < p-5 and p > 40:
            action = 2
        elif b > p+5 and p < 190:
            action = 5
    c = not c
    o, _, done, _ = env.step(action)
input("Press any key to continue")
