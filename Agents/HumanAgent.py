from Agents.IAgent import IAgent


class HumanAgent(IAgent):
    def __init__(self, name='1'):
        super().__init__(name)

    def do_move(self, game_class):
        allowed_moves = [i + 1 for i in range(9) if game_class.state[i] == ' ']
        human_move = None
        while not human_move:
            idx = int(input('Choose move for {}, from {} : '.format(game_class.player, allowed_moves)))
            if any([i == idx for i in allowed_moves]):
                human_move = idx
                #human_move = game_class.state[:idx - 1] + game_class.player + game_class.state[idx:]
        return human_move

    def __str__(self):
        return "Human " + self.name

