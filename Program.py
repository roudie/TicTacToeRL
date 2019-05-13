from Agents.RandomAgent import RandomAgent
from Agents.AgentQLearning import AgentQLearning
from GameCore.GameManagement import GameManagement
import FilesManagement
import pandas as pd
import matplotlib.pyplot as plt

def demo_games(agent1, agent2=RandomAgent(), n=100, show_result=True, generate_history=False, learn_agents=True):
    game = GameManagement(agent1, agent2)
    result = {agent1.__str__(): 0, agent2.__str__(): 0, 'draw': 0}
    history = []
    for i in range(n):
        single_game_result = game.start(show=False, learn_agents=learn_agents)
        result[single_game_result] += 1
        if generate_history:
            history+=game.history
    for key, val in result.items():
        result[key] = result[key]/n*100
    if show_result:
        print(result)
    return history, result


if __name__ == '__main__':
    agent1 = AgentQLearning(name = '1', learningRate = 0.9, discountFactor = 0.95)

    history = []
    result_df = pd.DataFrame()
    for i in range(100):
        print(i)
        hist, result = demo_games(agent1, n=100, show_result=False)
        history=history + hist
        hist, result = demo_games(agent1, n=10000, learn_agents=False, show_result=False)
        result['n'] = i*100 + 100
        result = pd.DataFrame([result])
        result_df = pd.concat([result_df, result])

    print(result_df)
    ax = plt.gca()
    result_df.plot(kind='line', x='n', y='draw', ax=ax)
    result_df.plot(kind='line', x='n', y='Agent Q-Learning 1', ax=ax)
    result_df.plot(kind='line', x='n', y='Random agent 1', ax=ax)

    plt.show()
    #FilesManagement.save(history, 'games.pkl')
    #data = FilesManagement.load('games.pkl')
    #print(data)



