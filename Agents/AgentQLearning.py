import csv
import random
from Agents.IAgent import IAgent
from Agents.QLearning import QLearning


class AgentQLearning(IAgent):

    def __init__(self, name='1', learningRate = 0.9, discountFactor = 0.9):
        super().__init__(name)
        self.QLearning = QLearning(game=None, learningRate=learningRate, discountFactor=discountFactor)

    def learning(self, game, last_player):
        self.QLearning.game = game
        self.QLearning.marker = self.marker
        self.QLearning.learn_move(game.last_state, game.last_move, last_player)

    def do_move(self, game):
        self.QLearning.game = game
        self.QLearning.marker = self.marker
        best_move = self.QLearning.get_best_move(game.state)
        if best_move is None:
            best_move = random.choice(game.allowed_next_moves())
        return best_move

    def __str__(self):
        return "Agent Q-Learning " + self.name
