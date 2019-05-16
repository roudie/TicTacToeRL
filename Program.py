from Agents.RandomAgent import RandomAgent
from Agents.AgentQLearning import AgentQLearning
from Agents.DTRAgent import DTRAgent
from GameCore.GameManagement import GameManagement
import FilesManagement
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

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
    agent2 = DTRAgent(name='1', maxDepth=20)

    history = []
    result_df = pd.DataFrame()
    for i in range(2):
        print(i)
        hist, result = demo_games(agent2, n=100, show_result=False)
        history=history + hist
        hist, result = demo_games(agent2, n=10000, learn_agents=False, show_result=False)
        result['n'] = i*100 + 100
        result = pd.DataFrame([result])
        result_df = pd.concat([result_df, result])

    print(result_df)
    ax = plt.gca()
    result_df.plot(kind='line', x='n', y='draw', ax=ax)
    result_df.plot(kind='line', x='n', y='Agent Q-Learning 1', ax=ax)
    result_df.plot(kind='line', x='n', y='Random agent 1', ax=ax)


    plt.show()
    hist, result = demo_games(agent2, n=100, show_result=False, generate_history=True)
    history = history + hist

    #FilesManagement.save(history, 'games.pkl')
    #data = FilesManagement.load('games.pkl')
    #print(len(data))

    # prepare dataframe
    #games_df = pd.read_csv('games.csv')
    #newgames_df = pd.DataFrame(history, columns=['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3', 'Result'])
    #games_df = pd.DataFrame(history, columns=['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3', 'Result'])
    #games_df = pd.merge(games_df, newgames_df)
    #games_df.to_csv('games.csv', index=False)

    # train sets
    #X_test_cls_char = games_df[games_df.columns[-1]][-20:]
    #games_df['Result'] = games_df['Result'].map({'_': 0, 'X': 1, 'O': 2})
    #games_df = games_df.astype(int)
    #X_train = games_df[games_df.columns[:-1]]
    #y_train = games_df[games_df.columns[-1]]

    # fit regression tree
    #regr = DecisionTreeRegressor(max_depth=20)
    #regr.fit(X_train, y_train)

    # predictions
    #X_test = games_df[games_df.columns[:-1]][-20:]
    #X_test_cls_num = games_df[games_df.columns[-1]][-20:]
    #y_test = regr.predict(X_test)
    #def to_class(n):
    #    classes = {0: '_', 1: 'X', 2: 'O'}
    #    return classes[n]
    #_test_cls_char = map(to_class, [int(round(i, 0)) for i in y_test])
    #print("Test num: ", X_test_cls_num.values.tolist())  # test num classes
    #print("Pred num: ", [int(round(i, 0)) for i in y_test])  # predicted num classes
    #print("Test char: ", X_test_cls_char.values.tolist())  # test char classes
    #print("Pred char: ", list(y_test_cls_char))  # predicted char classes



