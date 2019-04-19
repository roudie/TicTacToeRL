from Agents.RandomAgent import RandomAgent
from GameCore import TicTacToeGame
from Agents.AgentQLearning import AgentQLearning
from GameCore.GameManagement import GameManagement
from Agents.HumanAgent import HumanAgent
from GameCore.TicTacToeGame import TicTacToeGame
from pprint import pprint
import pandas as pd


def demo_game_stats1(agent):
    results = [agent.demo_game(TicTacToeGame) for i in range(10000)]
    game_stats = {k: results.count(k)/100 for k in ['X', 'O', '-']}
    print("    percentage results: {}".format(game_stats))

def demo_game_stats(agent1, agent2=RandomAgent(), n=5000):

    game = GameManagement(agent1, agent2)
    result = dict()

    for i in range(n):
        single_game_result = game.start(show=False)
        if result.get(single_game_result) is None:
            result[single_game_result] = 1
        else:
            result[single_game_result] += 1
    #data = pd.DataFrame(columns= [key for key, val in result.items()])
    for key, val in result.items():
        result[key] = result[key]/n*100

    pprint(result)

if __name__ == '__main__':
    agent1 = AgentQLearning(name = '1', epsilon = 0.01, alpha = 3.0)
    agent2 = HumanAgent()
    agent3 = HumanAgent()
    game = GameManagement(agent2, agent3)
    game.start(True)
    for i in range(50):
        agent1.learn_game(TicTacToeGame, 1000)
        game = GameManagement(agent1=agent1, agent2=agent2)
        #game.start(True)
        demo_game_stats(agent1)

