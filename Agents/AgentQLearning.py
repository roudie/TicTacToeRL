import csv
import random
from Agents.IAgent import IAgent
from Agents.QLearning import QLearning


class AgentQLearning(IAgent):
    last_move = None;
    def __init__(self, name='1', epsilon=0.01, alpha=1.0, learning=True):
        super().__init__(name)
        self.V = dict()
        self.epsilon = epsilon
        self.alpha = alpha
        self.learn = learning
        self.QLearning = QLearning(None)

    def learning(self, game, last_player):
        self.QLearning.game = game
        self.QLearning.marker = self.marker
        self.QLearning.learn_move(game.last_state, game.last_move, last_player)


    def do_move(self, game):
        self.QLearning.game = game
        self.QLearning.marker = self.marker

        #if game.last_move is not None:
        #    self.QLearning.learn_move(game.last_state, game.last_move)
        best_move = self.QLearning.get_best_move(game.state)
        if best_move is None:
            best_move = random.choice(game.allowed_next_moves())

        #self.QLearning.learn_move(game.state, best_move)
        return best_move
        #if self.learning:
        #    if game.get_last_move() is not None:
        #        return self.learn_from_move(game, game.get_last_move())
        #    else:
        #        _, move = self.learn_select_move(game)
        #        return move
        #else:
        #    return self.play_select_move(game)

    def state_value(self, game_state):
        return self.V.get(game_state, 0.0)

    def learn_game(self, game, num_episodes=1000):
        for episode in range(num_episodes):
            self.learn_from_episode(game)

    def learn_from_episode(self, game):
        game = game()
        _, move = self.learn_select_move(game)
        markers = ['O','X']
        curr = True
        while move:
            game.make_move(move, markers[curr])
            curr = not curr
            move = self.learn_from_move(game, move)

    def learn_from_move(self, game, move):
        #game.make_move(move)
        r = self.__reward(game)
        td_target = r
        next_state_value = 0.0
        selected_next_move = None
        if game.playable():
            best_next_move, selected_next_move = self.learn_select_move(game)
            next_state_value = self.state_value(best_next_move)
        current_state_value = self.state_value(move)
        td_target = r + next_state_value
        self.V[move] = (1-self.alpha) * current_state_value + self.alpha * (td_target - current_state_value)
        return selected_next_move

    def learn_select_move(self, game):
        allowed_state_values = self.__state_values(game.allowed_next_states())
        if game.player == self.marker:
            best_move = self.__argmax_V(allowed_state_values)
        else:
            best_move = self.__argmin_V(allowed_state_values)

        selected_move = best_move
        if random.random() < self.epsilon:
            selected_move = self.__random_V(allowed_state_values)

        return (best_move, selected_move)

    def play_select_move(self, game):
        allowed_state_values = self.__state_values(game.allowed_next_states())
        if game.player == self.marker:
            return self.__argmax_V(allowed_state_values)
        else:
            return self.__argmin_V(allowed_state_values)


    def demo_game(self, game, verbose=False):
        game = game()
        t = 0
        while game.playable():
            if verbose:
                print(" \nTurn {}\n".format(t))
                game.print_board()
            move = self.play_select_move(game)
            game.make_move(move)
            t += 1
        if verbose:
            print(" \nTurn {}\n".format(t))
            game.print_board()
        if game.winner:
            if verbose:
                print("\n{} is the winner!".format(game.winner))
            return game.winner
        else:
            if verbose:
                print("\nIt's a draw!")
            return '-'

    def round_V(self):
        # After training, this makes action selection random from equally-good choices
        for k in self.V.keys():
            self.V[k] = round(self.V[k],1)

    def save_v_table(self):
        with open('state_values.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['State', 'Value'])
            all_states = list(self.V.keys())
            all_states.sort()
            for state in all_states:
                writer.writerow([state, self.V[state]])

    def __state_values(self, game_states):
        return dict((state, self.state_value(state)) for state in game_states)

    def __argmax_V(self, state_values):
        max_V = max(state_values.values())
        chosen_state = random.choice([state for state, v in state_values.items() if v == max_V])
        return chosen_state

    def __argmin_V(self, state_values):
        min_V = min(state_values.values())
        chosen_state = random.choice([state for state, v in state_values.items() if v == min_V])
        return chosen_state

    def __random_V(self, state_values):
        return random.choice(list(state_values.keys()))

    def __reward(self, game):
        if game.winner == self.marker:
            return 1.0
        elif game.winner:
            return -1.0
        else:
            return 0.0

    def __str__(self):
        return "Agent Q-Learning " + self.name