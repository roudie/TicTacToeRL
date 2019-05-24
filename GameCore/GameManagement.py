import random
from GameCore.TicTacToeGame import TicTacToeGame


class GameManagement:
    def __init__(self, agent1, agent2):
        self.agents = [agent1, agent2]
        self.history = []

    def start(self, show=True, save_values=True, learn_agents=True, random_order=True):
        game = TicTacToeGame()
        self.history = []
        if random_order:
            self.currentAgentId = random.randint(0, 1)
        else:
            self.currentAgentId = 0
        if self.currentAgentId == 0:
            self.agents[0].set_marker('O')
            self.agents[1].set_marker('X')
        else:
            self.agents[0].set_marker('X')
            self.agents[1].set_marker('O')

        t = 1
        while game.playable():
            if show:
                print(" \nTurn {}\n".format(t))
                game.print_board()
            move = self.agents[self.currentAgentId].do_move(game)
            game.make_move(move, self.agents[self.currentAgentId].marker)
            self.history.append(self.state_to_array(game.state))
            if self.currentAgentId == 0:
                self.currentAgentId = 1
            else:
                self.currentAgentId = 0
            t += 1
            if learn_agents:
                self.agents[0].learning(game, game.last_player)
                self.agents[1].learning(game, game.last_player)

        if game.winner:
            if game.winner == self.agents[0].marker:
                winner = self.agents[0].__str__()
            else:
                winner = self.agents[1].__str__()
            if show:
                game.print_board()
                print("\n{}-{} is the winner!".format(game.winner, winner))
            self.add_winner_to_game_hist(game.winner)
            return winner
        if show:
            game.print_board()
            print("\nIt's a draw!")
        self.add_winner_to_game_hist('_')
        return 'draw'

    def state_to_array(self, state):
        ret_state = []
        for x in state:
            if x == ' ':
                ret_state.append(0)
            elif x == 'X':
                ret_state.append(1)
            else:
                ret_state.append(-1)
        return ret_state

    def add_winner_to_game_hist(self, winner):
        for x in self.history:
            x.append(winner)





