from Agents.IAgent import IAgent
from random import randint

class RandomAgent(IAgent):
    def __init__(self, name='1'):
        super().__init__(name)

    def do_move(self, game_class):
        allowed_moves = game_class.allowed_next_states()

        return allowed_moves[randint(0, len(allowed_moves)-1)]

    def __str__(self):
        return "Random agent " + self.name