
class IAgent:
    marker = None

    def __init__(self, name=''):
        self.name = name

    def do_move(self, game_class):
        pass

    def set_marker(self, marker):
        self.marker = marker

    def __str__(self):
        return "IAgent " + self.name

