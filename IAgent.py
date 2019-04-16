
class IAgent:
    def __init__(self, game_class, marker):
        self.game = game_class
        self.marker = marker

    def do_move(self):
        pass

    def set_marker(self, marker):
        self.marker = marker