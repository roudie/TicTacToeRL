import pickle

def save(data, file):
    #data = pd.DataFrame(data)
    with open(file, 'wb') as f:
        pickle.dump(data, f)

def load(file):
    with open(file, 'rb') as f:
        data = pickle.load(f)
    return data

if __name__ == '__main__':
    data = load('games.pkl')
    print(data)