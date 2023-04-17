import pandas as pd


def data_import():
    data_csv = pd.read_csv(r'./data/u.data', sep='\t', names=['user_id', 'movie_id', 'ranting', 'unix-timestamp'])
    return data_csv


def item_import():
    lis = [['movie_id', 'movie_name', 'time', 'unix-imdb_url'], list(range(5, 25))]
    item_csv = pd.read_csv(r'./data/u.item', sep="|", encoding="ISO-8859-1", names=lis[0]+lis[1])

    return item_csv


def user_import():
    user_csv = pd.read_csv(r'./data/u.user', sep="|", names=['user_id', 'age', 'sex', 'occupation', 'zip_code'])
    return user_csv


if __name__ == "__main__":
    # print(data_import())
    print(item_import())
    # print(user_import())
