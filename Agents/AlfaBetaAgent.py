from Agents.IAgent import IAgent
from random import randint
import numpy as np
import random


class AlfaBetaAgent(IAgent):
    game_class = None

    def __init__(self, name='1'):
        super().__init__(name)

    def do_move(self, game_class):
        allowed_moves = game_class.allowed_next_moves()
        self.game_class = game_class

        state = game_class.state
        move_values = []
        for move in allowed_moves:
            move_values.append(
                self.alfa_beta(
                    self.make_move(
                        self.game_class.state,
                        move,
                        self.marker),
                    self.change_player(self.marker),
                    -200,
                    200,
                    True))
        extremum = np.max(move_values)
        indices = [i for i in range(len(move_values)) if move_values[i] == extremum]
        choice = allowed_moves[random.choice(indices)]
        return choice

    def __str__(self):
        return "AlfaBeta " + self.name

    def alfa_beta(self, state, player, alfa, beta, maximizingPlayer):
        winner = self.game_class.predict_winner(state)

        available_moves = self.get_available_moves(state)

        if winner or len(available_moves)==0:
            if winner == self.marker:
                return 50 + len(available_moves)
            elif winner is not None:
                return -50 - len(available_moves)
            else:
                return 0
        if maximizingPlayer:
            value = -100
            for move in available_moves:
                value = max(alfa,
                           self.alfa_beta(
                               self.make_move(state, move, player),
                               self.change_player(player),
                               alfa,
                               beta,
                               False
                           ))
                alfa = max(alfa, value)
                #print('alpha ', alfa, '\t', 'beta: ', beta)
                if alfa >= beta:
                    break
            return value
        else:
            value = 100
            for move in available_moves:
                value = min(value,
                           self.alfa_beta(
                               self.make_move(state, move, player),
                               self.change_player(player),
                               alfa,
                               beta,
                               True
                           ))
                beta = min(beta, value)
                if alfa >= beta:
                    break
            return value

    @staticmethod
    def get_available_moves(state):
        moves = []
        for i in range(len(state)):
            if state[i] == ' ':
                moves.append(i + 1)
        return moves

    @staticmethod
    def make_move(state, move, player):
        return state[:move - 1] + player + state[move:]

    @staticmethod
    def change_player(player):
        if player == 'X':
            return 'O'
        return 'X'
