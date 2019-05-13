import random


class QLearning:
    marker = None

    def __init__(self, game, learningRate = 0.9, discountFactor = 0.9):
        self.QTable = dict()
        self.game = game
        self.learningRate = learningRate
        self.dicountFactor = discountFactor


    def learn_move(self, state, move, last_player):
        self.last_player = last_player
        if state not in self.QTable:
            self.QTable[state] = dict()
            #next_moves = self.game.allowed_next_moves()
            #for move_i in next_moves:
            self.QTable[state][move] = 0.1
        if move not in self.QTable[state]:
            self.QTable[state][move] = 0.1


        next_state = self.game.state

        #simulated_state = self.game.simulate(best_move)
        reward = self.get_reward(next_state)

        if next_state not in self.QTable:
            self.QTable[next_state] = dict()
            next_moves = self.game.allowed_next_moves()
            for move_i in next_moves:
                self.QTable[next_state][move_i] = 0.1

        best_move = self.get_best_move(next_state)



        self.QTable[state][move] = (1-self.learningRate)*self.QTable[state][move] + self.learningRate*(reward + self.dicountFactor * self.QTable[next_state][best_move])

        x = 3

    def get_best_move(self, state):
        if state not in self.QTable:
            return None
        #allowed_state_values = self.game.allowed_next_moves()
        #best_move = self.__argmax_V(allowed_state_values)
        if len(self.QTable[state].values()) == 0:
            self.QTable[state][0] = 0
            return 0
        if self.marker == 'X':
            max_V = max(self.QTable[state].values())
        else:
            max_V = min(self.QTable[state].values())
        max_list = []
        for key, val in self.QTable[state].items():
            if val == max_V:
                max_list.append([key, val])
        return random.choice(max_list)[0]
        #return best_move

    def get_reward(self, state):
        winner = self.game.predict_winner(state)
        if winner is not None:
            if winner == 'X':
                return 1.0
            else:
                return -1.0
        else:
            if len(self.game.allowed_next_moves()) == 0:
                return 0.0
            else:
                return 0.0

    def __argmax_V(self, state_values):
        max_V = max(state_values.values())
        chosen_state = random.choice([state for state, v in state_values.items() if v == max_V])
        return chosen_state

    def __argmin_V(self, state_values):
        min_V = min(state_values.values())
        chosen_state = random.choice([state for state, v in state_values.items() if v == min_V])
        return chosen_state