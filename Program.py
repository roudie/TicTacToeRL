import numpy as np

from itertools import groupby
import TicTacToeGame
import Agent

def demo_game_stats(agent):
    results = [agent.demo_game() for i in range(1000)]
    game_stats = {k: results.count(k)/100 for k in ['X', 'O', '-']}
    print("    percentage results: {}".format(game_stats))

if __name__ == '__main__':
    agent = Agent.Agent(TicTacToeGame.TicTacToeGame, epsilon = 0.1, alpha = 1.0)
    print("Before learning:")
    demo_game_stats(agent)
    agent.interactive_game()

    agent.learn_game(1000)
    print("After 1000 learning games:")
    demo_game_stats(agent)

    agent.learn_game(4000)
    print("After 5000 learning games:")
    demo_game_stats(agent)

    agent.learn_game(5000)
    print("After 10000 learning games:")
    demo_game_stats(agent)

    agent.learn_game(10000)
    print("After 20000 learning games:")
    demo_game_stats(agent)

    agent.learn_game(10000)
    print("After 30000 learning games:")
    demo_game_stats(agent)

    agent.round_V()
    agent.save_v_table()