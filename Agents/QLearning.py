
class QLearning:
    def __init__(self, learningRate = 0.1, discountFactor = 0.5)
        self.QTable = dict()
        self.learingRate = learningRate
        self.dicountFactor = discountFactor

    def learn_move(self, state, move):
        if self.QTable[state] is None:
            self.QTable[state] = dict()
        if self.QTable[state][move] is None:
            self.QTable[state][move] = 0
        reward = 0
        self.QTable[state][move] = (1-self.learingRate)*self.QTable[state][move] + self.learingRate*(reward + self.dicountFactor)