
import numpy as np
import random
from environment import Env
from collections import defaultdict

class QLearningAgent:
    def __init__(self, actions):
        # action = [0, 1, 2, 3] 순서대로 상, 하, 좌, 우
        self.actions = actions
        self.learning_rate = 0.01
        self.discount_factor = 0.9
        self.epsilon = 0.9
        self.q_table = defaultdict(lambda: [0.0, 0.0, 0.0, 0.0])

    def learn(self, state, action, reward, next_state):
        q_1 = self.q_table[state][action]
        # Bellman optimality equation을 사용하여 Q function update
        q_2 = reward + self.discount_factor * "?")
        self.q_table[state][action] += self.learning_rate * (q_2 - q_1)

    # epsilon-greedy policy에 따라서 action을 반환
    def get_action(self, state):
        if np.random.rand() < self.epsilon:
            action = np.random.choice(self.actions)
        else:
            state_action = self.q_table[state]
            action = self.arg_max(state_action)
        return action

    @staticmethod
    def arg_max(state_action):
        max_index_list = []
        max_value = state_action[0]
        for index, value in enumerate(state_action):
            if value > max_value:
                max_index_list.clear()
                max_value = value
                max_index_list.append(index)
            elif value == max_value:
                max_index_list.append(index)
        return random.choice(max_index_list)


if __name__ == "__main__":
    env = Env()
    agent = QLearningAgent(actions=list(range(env.n_actions)))

    for episode in range(1000):
        # initialize environment
        state = env.reset()

        while True:
            env.render()

            # 현재 state에서 action 선택 (ε-greedy)
            "?" = agent.get_action("?")
            
            "?", reward, done = env.step("?")

            # Q function를 update
            agent.learn("?", "?", reward, "?")
            
            state = "?"
            
            # 모든 Q function를 화면에 표시
            env.print_value_all(agent.q_table)

            if done:
                break
            
