import pandas as pd


def data_import():
    data_csv = pd.read_csv(r'./data/u.data', sep='\t', names=['user_id', 'movie_id', 'ranting', 'unix-timestamp'])
    return data_csv


def item_import():
    # 读取csv文件并为前四列设置一级标题，后20列设置二级标题
    item_csv = pd.read_csv('./data/u.item', sep='|', encoding='ISO-8859-1',
                           names=['movie_id', 'title', 'release_date', 'url'] + [i for i in range(20)],
                           usecols=list(range(24)))
    # 为前四列设置二级标题
    # item_csv.columns = pd.MultiIndex.from_product([['Movie_Info'], item_csv.columns])
    return item_csv


def user_import():
    user_csv = pd.read_csv(r'./data/u.user', sep="|", names=['user_id', 'age', 'sex', 'occupation', 'zip_code'])
    return user_csv


if __name__ == "__main__":
    # print(data_import())
    pd.set_option('display.max_columns', None)
    print(item_import())
    # print(user_import())
