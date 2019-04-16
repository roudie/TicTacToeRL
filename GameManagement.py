from random import random
from TicTacToeGame import TicTacToeGame
class GameManagement:

    def __init__(self, agent1, agent2):
        self.agents = [agent1, agent2]

    def start(self, show=True):
        game = TicTacToeGame()
        first_player = random.randint(0, 1)
        if first_player == 0:
            self.agents[0].set_marker('O')
            self.agents[1].set_marker('X')
            self.currentAgentId = 0;
        else:
            self.agents[0].set_marker('X')
            self.agents[1].set_marker('O')
            self.currentAgentId = 1;

        t = 1
        while game.playable():
            if show:
                print(" \nTurn {}\n".format(t))
                game.print_board()
            move = self.agents[self.currentAgentId].do_move()
            if self.currentAgentId == 0:
                self.currentAgentId = 1
            else:
                self.currentAgentId = 0
            t += 1

        if game.winner:
            print("\n{} is the winner!".format(game.winner))
            return game.winner
        print("\nIt's a draw!")
        return '-'






