import pandas as pd


def data_import():
    data_csv = pd.read_csv(r'./data/u.data', sep='\t', names=['user_id', 'movie_id', 'ranting', 'unix-timestamp'])
    return data_csv


def item_import():
    lis = ['movie_id', 'movie_name', 'time', 'unix-imdb_url', 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24]
    item_csv = pd.read_csv(r'./data/u.item', sep="|", encoding="ISO-8859-1",
                           names=lis)  # names=['movie_id','unix-imdb_url']
    return item_csv


def user_import():
    user_csv = pd.read_csv(r'./data/u.user', sep="|", names=['user_id', 'age', 'sex', 'occupation', 'zip_code'])
    return user_csv


if __name__ == "__main__":
    # print(data_import())
    print(item_import())
    # print(user_import())
