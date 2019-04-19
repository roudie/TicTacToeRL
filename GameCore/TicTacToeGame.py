class TicTacToeGame():
    last_move = None
    def __init__(self):
        self.state = '         '
        self.player = 'X'
        self.winner = None

    def allowed_next_states(self):
        states = []
        for i in range(len(self.state)):
            if self.state[i] == ' ':
                states.append(self.state[:i] + self.player + self.state[i+1:])
        return states

    def allowed_next_moves(self):
        moves = []
        for i in range(len(self.state)):
            if self.state[i] == ' ':
                moves.append(i+1)
        return moves

    def get_last_move(self):
        return self.last_move

    def make_move(self, next_move, marker):
        if self.winner:
            raise(Exception("Game already completed, cannot make another move!"))
        if self.state[next_move-1] != ' ':
            raise (Exception("Cannot make move {} to {} for player {}".format(
                self.state, next_move, self.player)))
        next_move = self.state[:next_move - 1] + self.player + self.state[next_move:]
        if not self.__valid_move(next_move):
            raise(Exception("Cannot make move {} to {} for player {}".format(
                    self.state, next_move, self.player)))
        self.last_move = next_move

        self.state = next_move
        self.winner = self.predict_winner(self.state)
        if self.winner:
            self.player = None
        elif self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def playable(self):
        return ((not self.winner) and any(self.allowed_next_states()))

    def predict_winner(self, state):
        lines = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        winner = None
        for line in lines:
            line_state = state[line[0]] + state[line[1]] + state[line[2]]
            if line_state == 'XXX':
                winner = 'X'
            elif line_state == 'OOO':
                winner = 'O'
        return winner

    def __valid_move(self, next_state):
        allowed_moves = self.allowed_next_states()
        if any(state == next_state for state in allowed_moves):
            return True
        return False

    def print_board(self):
        s = self.state
        print('     {} | {} | {} '.format(s[0],s[1],s[2]))
        print('    -----------')
        print('     {} | {} | {} '.format(s[3],s[4],s[5]))
        print('    -----------')
        print('     {} | {} | {} '.format(s[6],s[7],s[8]))