import random

class PollutionEnv:
    def __init__(self):
        self.state = 100

    def reset(self):
        self.state = random.randint(60, 100)
        return self.state

    def step(self, action):
        if action == 1:
            self.state -= 5
        elif action == 2:
            self.state -= 10
        else:
            self.state += 2

        self.state = max(0, min(100, self.state))

        reward = 100 - self.state
        done = self.state < 10

        return self.state, reward, done, {"pollution": self.state}