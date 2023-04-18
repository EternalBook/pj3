# 科学计算相关库引入
import pandas as pd

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
    data_csv = data_import()

    """
    2.电影数据处理
    """
    # # 查看表结构
    # print(item_import().head())
    # # 查看数据表的信息  可以查看是否存在缺失值，
    # print(item_import().info())
    # # 3.1查看是否存在缺失值      结论: video_release_date列无数据 直接删除 对于title数据为unknown的直接删除行  unix-imdb_url/release_date 不需要处理
    # print(item_import().isnull().any())
    item_csv = item_import().drop("video_release_date", axis=1)
    print(item_csv[item_csv.isnull().values == True])
    # # 3.2 查看是否存在重复值 根据业务而定，评分人群是一个范围值，而不是具体特质的人
    # # 3.3 查看是否异常值 根据业务而定，年龄和性别是涉及到后续的特征提取       设置了数据范围==========年龄（6，75），性别（F/M)
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
    user_csv = user_import()

    # # 4.三张表进行合并 合并方式：外联 条件合并：两两合并
    # df1 = pd.merge(user_import(), data_import(), how='outer')
    # lens = pd.merge(df1, item_import(), how="outer")
    # print(lens.head())
