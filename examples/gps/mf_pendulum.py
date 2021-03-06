import gym
from trajopt.gps import MFGPS


# pendulum env
env = gym.make('Pendulum-TO-v0')
env._max_episode_steps = 100
env.unwrapped._dt = 0.05

alg = MFGPS(env, nb_steps=100,
            kl_bound=1.,
            init_ctl_sigma=2.5,
            activation={'shift': 90, 'mult': 2.})

# run gps
trace = alg.run(nb_episodes=10)

# plot dists
alg.plot()

# execute and plot
nb_episodes = 25
data = alg.sample(nb_episodes, stoch=False)

import matplotlib.pyplot as plt

plt.figure()
for k in range(alg.dm_state):
    plt.subplot(alg.dm_state + alg.dm_act, 1, k + 1)
    plt.plot(data['x'][k, ...])

for k in range(alg.dm_act):
    plt.subplot(alg.dm_state + alg.dm_act, 1, alg.dm_state + k + 1)
    plt.plot(data['u'][k, ...])

plt.show()

# plot objective
plt.figure()
plt.plot(trace)
plt.show()
