import csv
import itertools
import pprint
from copy import copy, deepcopy

from Agents.RandomAgent import RandomAgent
from Agents.AgentQLearning import AgentQLearning
from Agents.DTRAgent import DTRAgent
from Agents.AlfaBetaAgent import AlfaBetaAgent
from GameCore.GameManagement import GameManagement
import pandas as pd
import matplotlib.pyplot as plt
import os
from tqdm import tqdm


def demo_games(agent1, agent2=RandomAgent(), n=100, show_result=True, generate_history=False, learn_agents=True, random_order=True):
    game = GameManagement(agent1, agent2)
    result = {agent1.__str__(): 0, agent2.__str__(): 0, 'draw': 0}
    history = []
    for iter in tqdm(range(n)):
        single_game_result = game.start(show=False, learn_agents=learn_agents, random_order=random_order)
        result[single_game_result] += 1
        if generate_history:
            history+=game.history
    for key, val in result.items():
        result[key] = result[key]/n*100
    if show_result:
        print(result)
    return history, result


if __name__ == '__main__':
        DTRAgents = []
        for filename in os.listdir('dataset'):
            DTRAgents.append(DTRAgent(name=filename,  maxDepth=30, file_name=('dataset/'+filename)))

        random_agent = RandomAgent()
        alfa_beta_agent = AlfaBetaAgent()

        QLearning_agents = []
        for i in range(1, 10):
            agent = AgentQLearning(name='R' + str((i)) + 'k', discountFactor=0.9, learningRate=0.9);
            _, result = demo_games(agent, random_agent, n=(i)*1000, show_result=False, learn_agents=True, random_order=False)
            QLearning_agents.append(agent)


        agents = [random_agent, alfa_beta_agent] + DTRAgents + QLearning_agents
        results = []

        n = len(agents)

        for i in range(n+1):
            results.append([None])
            for j in range(n+1):
                results[i].append([None]*3)
        for i in range(n):
            results[i+1][0] = agents[i].__str__()
            results[0][i+1] = agents[i].__str__()
        buff = deepcopy(results)

        for i in range(n):
            for j in range(n):
                if i == j:
                    results[i+1][j+1][0] = 0
                    results[i+1][j+1][1] = 0
                    results[i+1][j+1][2] = 0
                else:
                    _, result = demo_games(agents[i], agents[j], n=1000, show_result=False, learn_agents=False, random_order=False)
                    results[i+1][j+1][0] = result[agents[i].__str__()]
                    results[i+1][j+1][1] = result[agents[j].__str__()]
                    results[i+1][j+1][2] = result['draw']

        win_arr = deepcopy(buff)
        lost_arr = deepcopy(buff)
        draw_arr = deepcopy(buff)
        for i in range(1, len(results)):
            for j in range(1, len(results)):
                win_arr[i][j] = results[i][j][0]
                lost_arr[i][j] = results[i][j][1]
                draw_arr[i][j] = results[i][j][2]

        wtr = csv.writer(open('win.csv', 'w'), delimiter=';', lineterminator='\n')
        for x in win_arr:
            wtr.writerow(x)

        wtr = csv.writer(open('lost.csv', 'w'), delimiter=';', lineterminator='\n')
        for x in lost_arr:
            wtr.writerow(x)

        wtr = csv.writer(open('draw.csv', 'w'), delimiter=';', lineterminator='\n')
        for x in draw_arr:
            wtr.writerow(x)

        """for agent in DTRAgents:
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
    """