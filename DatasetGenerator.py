import os
from Agents.AgentQLearning import AgentQLearning
from Agents.RandomAgent import RandomAgent
import Program
import pandas as pd
def gen_dataset():
    dirName = 'dataset'
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    else:
        print("Directory ", dirName, " already exists")

    agent1 = AgentQLearning(name ='1', learningRate = 0.9, discountFactor = 0.95)

    Program.demo_games(agent1, n=10000, learn_agents=True, show_result=False)
    history = []
    for i in range(10):
        hist, _ = Program.demo_games(agent1, n=10000, learn_agents=False, show_result=False, generate_history=True)
        history = history + hist
        games_df = pd.DataFrame(history, columns=['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3', 'Result'])
        file_name = dirName + '/'+str((i+1)*10000) + '.csv'
        games_df.to_csv(file_name, index=False)
        print(file_name + ' created')


if __name__ == '__main__':
    gen_dataset()
