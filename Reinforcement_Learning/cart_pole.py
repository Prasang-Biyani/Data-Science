import gym
env = gym.make('CartPole-v0')
env.reset()
goal_steps = 500
score_requirement = 50
inital_games = 10000

def some_random_games_first():
    for episode in range(5):
        env.reset()
        for t in range(goal_steps):
            env.render()
            action = env.action_space.sample()
            observations, reward, done, info = env.step(action)
            print(observations)
            if done:
                break
    env.close()
some_random_games_first()
