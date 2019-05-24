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
from Program import demo_games as demo_games
if __name__ == '__main__':
    filename = 'random_100k.csv'
    agent = (DTRAgent(name=filename, maxDepth=30, file_name=filename))
    _, result = demo_games(agent, n=10000, show_result=True, learn_agents=True, random_order=False)
