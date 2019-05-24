import os
from Agents.AgentQLearning import AgentQLearning
from Agents.RandomAgent import RandomAgent
from Agents.AlfaBetaAgent import AlfaBetaAgent
import Program
import pandas as pd

def gen_dataset2():
    history = []
    agent = RandomAgent()
    hist, _ = Program.demo_games(agent, n=100000, learn_agents=False, show_result=False, generate_history=True)
    games_df = pd.DataFrame(hist, columns=['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3', 'Result'])
    file_name = 'random_100k.csv'
    games_df.to_csv(file_name, index=False)
    print('\n'+file_name + ' created')



def gen_dataset1():
    dirName = 'dataset1'
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    else:
        print("Directory ", dirName, " already exists")
    agent = AgentQLearning(name ='1', learningRate = 0.1, discountFactor = 0.1)
    Program.demo_games(agent, n=10000, learn_agents=True, show_result=False)

    history = []


    for i in range(9):
        hist, _ = Program.demo_games(agent, n=10000, learn_agents=False, show_result=False, generate_history=True)
        history = history + hist
        games_df = pd.DataFrame(history, columns=['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3', 'Result'])
        file_name = dirName + '/QL_10k_R_'+str((i+1)*10000) + '.csv'
        games_df.to_csv(file_name, index=False)
        print('\n'+file_name + ' created')

    
def gen_dataset():
    dirName = 'dataset'
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    else:
        print("Directory ", dirName, " already exists")

    agent = AgentQLearning(name ='1', learningRate = 0.9, discountFactor = 0.95)

    Program.demo_games(agent, n=1000, learn_agents=True, show_result=False)
    history = []
    for i in range(5):
        hist, _ = Program.demo_games(agent, n=1000, learn_agents=False, show_result=False, generate_history=True)
        history = history + hist
        games_df = pd.DataFrame(history, columns=['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3', 'Result'])
        file_name = dirName + '/QL_1k_R_'+str((i+1)*1000) + '.csv'
        games_df.to_csv(file_name, index=False)
        print('\n'+file_name + ' created')

    history = []
    agent = AgentQLearning(name='1', learningRate=0.9, discountFactor=0.95)
    Program.demo_games(agent, n=10000, learn_agents=True, show_result=False)
    for i in range(5):
        hist, _ = Program.demo_games(agent, n=1000, learn_agents=False, show_result=False, generate_history=True)
        history = history + hist
        games_df = pd.DataFrame(history, columns=['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3', 'Result'])
        file_name = dirName + '/QL_10k_R_'+str((i+1)*1000) + '.csv'
        games_df.to_csv(file_name, index=False)
        print('\n'+file_name + ' created')

    history = []
    agent = AlfaBetaAgent(name='1')
    for i in range(5):
        hist, _ = Program.demo_games(agent, n=1000, learn_agents=False, show_result=False, generate_history=True)
        history = history + hist
        games_df = pd.DataFrame(history, columns=['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3', 'Result'])
        file_name = dirName + '/AB_R_'+str((i+1)*1000) + '.csv'
        games_df.to_csv(file_name, index=False)
        print('\n'+file_name + ' created')

    history = []
    agent = RandomAgent()
    for i in range(5):
        hist, _ = Program.demo_games(agent, n=1000, learn_agents=False, show_result=False, generate_history=True)
        history = history + hist
        games_df = pd.DataFrame(history, columns=['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3', 'Result'])
        file_name = dirName + '/R_R_'+str((i+1)*1000) + '.csv'
        games_df.to_csv(file_name, index=False)
        print('\n'+file_name + ' created')


if __name__ == '__main__':
    gen_dataset2()
