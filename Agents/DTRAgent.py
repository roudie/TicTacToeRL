from Agents.IAgent import IAgent
import random
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

class DTRAgent(IAgent):

    def __init__(self, name='1', maxDepth=20):
        super().__init__(name)
        self.DTR = DecisionTreeRegressor(max_depth=maxDepth)  # Decision Tree Regressor

        # learning by data from last games
        games_df = pd.read_csv('games.csv')
        games_df['Result'] = games_df['Result'].map({'_': 0, 'X': 1, 'O': 2})
        games_df = games_df.astype(int)
        X_train = games_df[games_df.columns[:-1]]
        y_train = games_df[games_df.columns[-1]]

        self.DTR.fit(X_train, y_train)

    def learning(self, game, last_player):
        pass
        #self.QLearning.game = game
        #self.QLearning.marker = self.marker
        #self.QLearning.learn_move(game.last_state, game.last_move, last_player)

    def do_move(self, game):
        available_states, available_moves = game.allowed_next_states(), game.allowed_next_moves()
        #print(game.player, "State: ", game.state)
        #print("Next available_states: ", available_states)
        print("Next available_moves: ", available_moves)
        # list of lists of states to prediction
        test_states = [[{' ': 0, 'X': 1, 'O': 2}[pos] for pos in st] for st in available_states]
        #print("Test states:", test_states)
        predicted = self.DTR.predict(test_states)
        predicted = [int(round(i, 0)) for i in predicted]
        predicted = [-1 if i == 2 else i for i in predicted]
        #print("Predictions:", predicted)
        # if 'X' select all max_value indices, else min_value indices
        if (game.player == 'X'):
            indices = [i for i in range(len(predicted)) if predicted[i] == np.max(predicted)]
        else:
            indices = [i for i in range(len(predicted)) if predicted[i] == np.min(predicted)]
        print("Best moves indices:", indices)
        chosen = random.choice(indices)
        print("Chosen: index move", chosen, available_moves[chosen])
        return chosen

    def __str__(self):
        return "Agent DecisionTreeRegressor " + self.name
