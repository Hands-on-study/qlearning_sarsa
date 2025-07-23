
import numpy as np
import random
from collections import defaultdict
from environment import Env


class SARSAgent:
    def __init__(self, actions):
        # action = [0, 1, 2, 3] 순서대로 상, 하, 좌, 우
        self.actions = actions
        self.learning_rate = 0.01
        self.discount_factor = 0.9
        self.epsilon = 0.1
        self.q_table = defaultdict(lambda: [0.0, 0.0, 0.0, 0.0])


    def learn(self, state, action, reward, next_state, next_action):
        current_q = self.q_table[state][action]
        next_state_q = self.q_table[next_state][next_action]
        new_q = (current_q + self.learning_rate *
                ("?"))
        self.q_table[state][action] = new_q

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
    agent = SARSAgent(actions=list(range(env.n_actions)))

    for episode in range(1000):
        # initialize environment
        state = env.reset()

        # 현재 state에서 action 선택 (ε-greedy)
        action = agent.get_action("?")

        while True:
            env.render()

            "?", reward, done = env.step("?")
            
            "?" = agent.get_action("?")

            # Q function를 update
            agent.learn("?", "?", reward, "?", "?")

            state = "?"
            action = "?"

            # 모든 Q function를 화면에 표시
            env.print_value_all(agent.q_table)

            if done:
                break
