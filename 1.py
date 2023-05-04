# 科学计算相关库引入
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体，SimHei是中文黑体的意思
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题
'''
数据分析的指标
    1.哪些电影最受人关注（前20）
    2.
'''
"""
一、数据准备
"""


def data_import():
    # 1.定义评分数据表头
    data_csv = pd.read_csv(r'./data/u.data', sep='\t', names=['user_id', 'movie_id', 'ranting', 'unix-timestamp'],
                           encoding='latin-1')
    # data_csv.to_excel(r'./data/excel/data.xlsx')
    return data_csv


def item_import():
    # 设置评分数据表头
    item_csv = pd.read_csv('./data/u.item', sep='|', encoding='latin-1', usecols=range(5),
                           names=['movie_id', 'title', 'release_date', 'video_release_date', 'unix-imdb_url'])
    # item_csv.to_excel(r'./data/excel/item.xlsx')
    return item_csv


"""
3.用户信息读取
"""


def user_import():
    # 3.定义用户信息表头
    user_csv = pd.read_csv(r'./data/u.user', sep="|", names=['user_id', 'age', 'sex', 'occupation', 'zip_code'],
                           encoding='latin-1')
    # user_csv.to_excel(r'./data/excel/user.xlsx')
    return user_csv


if __name__ == "__main__":
    """
    1.评分数据处理
    """
    # # 查看表结构
    # print(data_import().head())
    # # 查看数据表的信息  可以查看是否存在缺失值，可以查看数据量
    # print(data_import().info())
    # # 1.1查看是否存在缺失值      结论: 数据表不存在缺失值
    # print(data_import().isnull().any())
    # # # 1.2 查看是否存在重复值 根据业务而定，评分值是一个范围不需要去重
    # # # 1.3 查看是否异常值 根据业务而定，评分是1-5分 结论 是没有异常值的
    # print(data_import().ranting.unique())
    # print(data_import())
    data_df = data_import()

    """
    2.电影数据处理
    """
    # # 查看表结构
    # print(item_import().head())
    # # 查看数据表的信息  可以查看是否存在缺失值，
    # print(item_import().info())
    # # 3.1查看是否存在缺失值      结论: video_release_date列无数据 直接删除  unix-imdb_url/release_date 不需要处理
    # print(item_import().isnull().any())
    item_df = item_import().drop("video_release_date", axis=1)
    # # 3.2 查看是否存在重复值 根据业务而定，不需要去除重复值
    # # 3.3 查看是否异常值 根据业务而定，
    # print(item_import().isnull().any())
    # print(item_import())
    # # 年龄（6，75)
    # print(user_import().age.unique())
    # # 性别(F/M) ['F','M']结论：用户数据表中，性别不纯在异常值，均为男性或者女性
    # print(user_import().sex.unique())
    # # print(user_import())

    # print(item_import())

    """
    3.用户信息处理
    """
    # # 查看表结构
    # print(user_import().head())
    # # 查看数据表的信息  可以查看是否存在缺失值，可以查看数据量
    # print(user_import().info())
    # # 3.1查看是否存在缺失值      结论: 数据表不存在缺失值
    # print(user_import().isnull().any())
    # # 3.2 查看是否存在重复值 根据业务而定，评分人群是一个范围值，而不是具体特质的人
    # # 3.3 查看是否异常值 根据业务而定，年龄和性别是涉及到后续的特征提取       设置了数据范围==========年龄（6，75），性别（F/M)
    # # 年龄（6，75)
    # print(user_import().age.unique())
    # # 性别(F/M) ['F','M']结论：用户数据表中，性别不纯在异常值，均为男性或者女性
    # print(user_import().sex.unique())
    # # print(user_import())
    user_df = user_import()

    # 4.三张表进行合并 合并方式：外联 条件合并：两两合并
    df1 = pd.merge(user_import(), data_import(), how='outer')
    lens = pd.merge(df1, item_import(), how="outer")
    lens.to_excel(r'./data/excel/lens.xlsx')
    # print(lens.head())
    # print(lens)
    # ======数据处理======
    # 删除表格中的空数据
    lens.dropna(1, how="all", inplace=True)
    # 查看数据量和列
    # print(lens.shape)
    # print(lens[["age", "ranting"]].describe())
    # 性别分组统计
    # print(lens["sex"].value_counts())
    # 计算每一列的空值
    total_null = lens.isnull().sum()
    # print(total_null)
    # total_null = lens.isnull().sum()
    # =============数据特征提取================
    # 1、哪些电影最受人关注？（前20）   绘图：前二十部电影（X），关注度（Y）
    print(lens.groupby("title").groups)
    most_rated = lens.groupby("title").size().sort_values(ascending=False)[:20]
    print(most_rated)
    # 2、哪些电影评分更高？（前50）    注意：评分人数太少，数据结果不具有参考价值   人数>100   绘图：前五十部电影（X），评分（Y）
    most_movie = lens.groupby("title").agg({'ranting': ["size", "mean"]})
    print(most_movie.sort_values(by="title",ascending=False))
    atleast = most_movie['ranting']['size'] >= 100
    most_50 = most_movie[atleast].sort_values(by=('ranting', 'mean'), ascending=False)[:50]
    print(most_50)
    # 3、电影的评分与年龄有关吗？
    user_df.age.plot.hist(bins=10)
    plt.title("电影的评分与年龄的关系")
    plt.ylabel("用户数量")
    plt.xlabel("年龄")
    # 看年龄的最大最小值
    print(user_df.age.min())
    print(user_df.age.max())
    # 4、电影的评分与性别有关吗
    pivoted = lens.pivot_table(index=['movie_id', 'title'],
                               columns=['sex'],
                               values='ranting',
                               fill_value=0)
    print(pivoted.head())
    pivoted['diff'] = pivoted.M - pivoted.F
    print(pivoted.head())
    # 设置movie_id为列
    pivoted.reset_index('movie_id', inplace=True)
    print(pivoted.head())
    # 查询前50部电影的数据
    df = DataFrame(pivoted.movie_id)
    disagreement = pivoted[df.index.isin(most_50.index)]["diff"].sort_values()
    plt.barh(most_50.index, disagreement)
    plt.title('男性和女性对电影评分的影响，大于0为男性，小于0为女性')
    plt.ylabel("电影名称")
    plt.xlabel("男女评分差值")
    plt.show()
