from Agents.IAgent import IAgent
from random import randint


class MinMaxAgent(IAgent):
    def __init__(self, name='1'):
        super().__init__(name)

    def do_move(self, game_class):
        allowed_moves = game_class.allowed_next_moves()

        return allowed_moves[randint(0, len(allowed_moves)-1)]

    def __str__(self):
        return "MinMax agent " + self.name

    def minmax(self, game_class, state, depth, player):
        """
        Recursively analyze every possible game state and choose
        the best move location.
        node - the board
        depth - how far down the tree to look
        player - what player to analyze best move for (currently setup up ONLY for "O")
        """
        if depth == 0 or game_class.predict_winner(state) is not None:
            if game_class.predict_winner(state) == "X":
                return 0
            elif game_class.predict_winner(state) == "O":
                return 100
            else:
                return 50

        if player == "O":
            best_value = 0
            for move in self.get_available_moves(state):
                node.makeMove(move, player)
                move_value = self.minimax(node, depth - 1, changePlayer(player))
                node.makeMove(move, " ")
                best_value = max(best_value, move_value)
            return best_value

        if player == "X":
            best_value = 100
            for move in node.availableMoves():
                node.makeMove(move, player)
                move_value = self.minimax(node, depth - 1, changePlayer(player))
                node.makeMove(move, " ")
                best_value = min(best_value, move_value)
            return best_value

    def get_available_moves(self, state):
        moves = []
        for i in range(len(self.state)):
            if state[i] == ' ':
                moves.append(i + 1)
        return moves

    def make_move(self, state, move):
        
