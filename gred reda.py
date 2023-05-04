import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

'''
数据分析指标
  1、哪些电影最受人关注？（前20）
  2、哪些电影评分更高（前50）
  3、电影的评分与年龄、性别有关吗？
'''

u_col = ["use_id", "age", "sex", "occuption", "zip_code"]
users = pd.read_csv(r"D:\pandas\专周实训\u.user", sep="|", names=u_col, encoding="latin-1")
# 查看表结构
print(users.head())
# 查看数据表的信息
print(users.info)
# 1.1查看是否存在缺失值  结论：数据表中不存在缺失数据
print(users.isnull().any())
# 1.2查看是否存在重复值   根据业务而定，评分人群是一个范围值，并不是具体特指的人
# 1.3查看是否存在异常值   根据业务而定，年龄和性别是涉及到后续的特征提取，  设置了数据=====年龄（6，75），性别（F/M）
# 年龄（6，75）
print(users.age.unique())
# 性别（F/M）
print(users.sex.unique())

# 2.影评数据读取
r_col = ["use_id", "movie_id", "rating", "unix_timestamp"]
ratings = pd.read_csv(r"D:\pandas\专周实训\u.data", sep="|", names=r_col, encoding="latin-1")
# 查看数据表
print(ratings.head())
# 查看数据表的信息
print(ratings.info)

# 3.电影信息读取
m_col = ["movie_id", "title", "release_time", "video_release_data", "imdb_url"]
movies = pd.read_csv(r"D:\pandas\专周实训\u.item", sep="|", names=m_col, encoding="latin-1", usecols=range(5))
# 查看表数据
print(movies.head())

# 4.三张表进行合并  合并方式外连   合并条件：两两合并
df1 = pd.merge(users, ratings, how='outer')
lens=pd.merge(df1,movies,how='outer')
print(df1)
print(lens.head())
# ======数据处理======
# 删除表格中的空数据
lens.dropna(1,how="all",inplace=True)
# 查看数据量和列
print(lens.shape)
print(lens[["age","rating"]].describe())
# 性别分组统计
print(lens["sex"].value_counts())
# 计算每一列的空值
total_null=lens.isnull().sum()
print(total_null)
total_null=lens().sum()

# =============数据特征提取================
# 1、哪些电影最受人关注？（前20）   绘图：前二十部电影（X），关注度（Y）
print(lens.groupby("title").groups)
most_rated=lens.groupby("title").size().sort_values(ascending=False)[:20]
print(most_rated)
# 2、哪些电影评分更高？（前50）    注意：评分人数太少，数据结果不具有参考价值   人数>100   绘图：前五十部电影（X），评分（Y）
most_movie=lens.groupby("title").agg({'rating':["size","mean"]})
print(most_movie.sort_values(ascending=False))
atleast=most_movie['rating']['size']>=100
most_50=most_movie[atleast].sort_values(['rating','mean'],ascending=False)[:50]
print(most_50)
# 3、电影的评分与年龄有关吗？
users.age.plot.hist(bins=10)
plt.title("电影的评分与年龄的关系")
plt.ylabel("用户数量")
plt.xlabel("年龄")
# 看年龄的最大最小值
print(users.age.min())
print(users.age.max())
# 4、电影的评分与性别有关吗
pivoted=lens.pivot_table(index=['movie_id','title'],
                 columns=['sex'],
                 values='rating',
                 fill_value=0)
print(pivoted.head())
pivoted['diff']=pivoted.M-pivoted.F
print(pivoted.head())
# 设置movie_id为列
pivoted.reset_index('movie_id',inplace=True)
print(pivoted.head())
#查询前50部电影的数据
df=DataFrame(pivoted.movie_id)
disagreement=pivoted[df.index.isin(most_50.index)]["diff"].sort_values()
plt.barh(most_50.index,disagreement)
plt.title('男性和女性对电影评分的影响，大于0为男性，小于0为女性')
plt.ylabel("电影名称")
plt.xlabel("男女评分差值")
plt.show()
