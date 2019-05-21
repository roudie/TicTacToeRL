import pickle


def save(data, file):
    with open(file, 'wb') as f:
        pickle.dump(data, f)


def load(file):
    with open(file, 'rb') as f:
        return pickle.load(f)


if __name__ == '__main__':
    data = load('games.pkl')
    print(data)
