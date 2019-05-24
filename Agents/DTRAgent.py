from Agents.IAgent import IAgent
import random
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

class DTRAgent(IAgent):

    def __init__(self, name='1', maxDepth=20, file_name='games.csv'):
        super().__init__(name)
        self.DTR = DecisionTreeRegressor(max_depth=maxDepth)  # Decision Tree Regressor

        # learning by data from last games
        games_df = pd.read_csv(file_name)
        games_df['Result'] = games_df['Result'].map({'_': 0, 'X': 1, 'O': -1})
        games_df = games_df.astype(int)
        x_train = games_df[games_df.columns[:-1]]
        y_train = games_df[games_df.columns[-1]]

        self.DTR.fit(x_train, y_train)

    def learning(self, game, last_player):
        pass

    def do_move(self, game):
        available_states, available_moves = game.allowed_next_states(), game.allowed_next_moves()
        test_states = [[{' ': 0, 'X': 1, 'O': -1}[pos] for pos in st] for st in available_states]
        predicted = self.DTR.predict(test_states)
        if game.player == 'O':
            indices = [i for i in range(len(predicted)) if predicted[i] == np.min(predicted)]
        else:
            indices = [i for i in range(len(predicted)) if predicted[i] == np.max(predicted)]

        return available_moves[random.choice(indices)]

    def __str__(self):
        return "DTR " + self.name
