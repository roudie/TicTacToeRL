import random


class QLearning:
    marker = None

    def __init__(self, game, learningRate = 0.9, discountFactor = 0.6):
        self.QTable = dict()
        self.game = game
        self.learningRate = learningRate
        self.dicountFactor = discountFactor


    def learn_move(self, state, move):
        if state not in self.QTable:
            self.QTable[state] = dict()
        if move not in self.QTable[state]:
            self.QTable[state][move] = 0

        best_move = self.get_best_move(state)
        simulated_state = self.game.simulate(best_move)
        reward = self.get_reward(simulated_state)

        #if simulated_state not in self.QTable:
        #    self.QTable[simulated_state] = dict()
        #if best_move not in self.QTable[simulated_state]:
        #    self.QTable[simulated_state][best_move] = 0

        self.QTable[state][move] = (1-self.learningRate)*self.QTable[state][move] + self.learningRate*(reward + self.dicountFactor * best_move)

        x = 3

    def get_best_move(self, state):
        if state not in self.QTable:
            return None
        max_V = max(self.QTable[state].values())
        max_list = []
        for key, val in self.QTable[state].items():
            if val == max_V:
                max_list.append([key, val])
        return random.choice(max_list)[0]

    def get_reward(self, state):
        winner = self.game.predict_winner(state)
        if winner == self.marker:
            return 50.0
        elif winner:
            return -1.0
        else:
            return 0.1

    def __argmax_V(self, state_values):
        max_V = max(state_values.values())
        chosen_state = random.choice([state for state, v in state_values.items() if v == max_V])
        return chosen_state

    def __argmin_V(self, state_values):
        min_V = min(state_values.values())
        chosen_state = random.choice([state for state, v in state_values.items() if v == min_V])
        return chosen_state