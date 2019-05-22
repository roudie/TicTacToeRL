from Agents.RandomAgent import RandomAgent
from Agents.AgentQLearning import AgentQLearning
from Agents.DTRAgent import DTRAgent
from Agents.AlfaBetaAgent import AlfaBetaAgent
from GameCore.GameManagement import GameManagement
import pandas as pd
import matplotlib.pyplot as plt
import os
from tqdm import tqdm


def demo_games(agent1, agent2=RandomAgent(), n=100, show_result=True, generate_history=False, learn_agents=True):
    game = GameManagement(agent1, agent2)
    result = {agent1.__str__(): 0, agent2.__str__(): 0, 'draw': 0}
    history = []
    for iter in tqdm(range(n)):
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
    agent4 = AlfaBetaAgent(name='x')
    hist, result = demo_games(agent4, n=20000, show_result=True, learn_agents=True)
    DTRAgents = []
    for filename in os.listdir('dataset'):
        DTRAgents.append(DTRAgent(name=filename,  maxDepth=30, file_name='dataset/'+filename))

    history = []
    result_df = pd.DataFrame()
    step = 100
    sim_amount = 100
    n = 10
    for agent in DTRAgents:
        result = []
        for i in tqdm(range(n)):
            #print(i)
            hist, result = demo_games(agent1, n=step, show_result=False, learn_agents=True)

            hist, result = demo_games(agent, agent1, n=sim_amount, learn_agents=False, show_result=False)
            result['n'] = i*step + step
            result = pd.DataFrame([result])
            result_df = pd.concat([result_df, result], sort=True)

        print(result_df)
        ax = plt.gca()
        for y in result_df.columns:
            if y != 'n':
                result_df.plot(kind='line', x='n', y=y, ax=ax)
        plt.savefig('fig/' + agent.__str__())
