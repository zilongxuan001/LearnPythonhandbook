import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties




df = pd.read_csv("d:/数据分析/DataAnalyst.csv",encoding = 'gb2312')
df
df.info()
df.head()
df.tail()

df.positionId.unique()
df_duplicates=df.drop_duplicates(subset='positionId',keep="first")
df_duplicates.head(5)
df_duplicates.info()

# 简版
# def cut_word(word):
#     position = word.find("-")
#     bottomSalary = word[:position-1]
#     return bottomSalary
# df_duplicates.salary.apply(cut_word)

# 只处理bottomSalary
# def cut_word(word):
#     position = word.find("-")
#     if position != -1:
#         bottomSalary = word[:position-1]
#     else:
#         bottomSalary = word[:word.upper().find('K')]
#     return bottomSalary
# df_duplicates['bottomSalary']=df_duplicates.salary.apply(cut_word)

def cut_word(word, method):
    position = word.find("-")
    length = len(word)
    if position != -1:
        bottomSalary = word[:position-1]
        topSalary= word[position+1:length-1]
    else:
        bottomSalary = word[:word.upper().find('K')]
        topSalary = bottomSalary
    if method == 'bottom':
        return bottomSalary
    else:
        return topSalary

df_duplicates['bottomSalary']=df_duplicates.salary.apply(cut_word, method="bottom")
df_duplicates['topSalary']=df_duplicates.salary.apply(cut_word,method="top")   
df_duplicates.topSalary = df_duplicates.topSalary.astype('int')
df_duplicates.bottomSalary= df_duplicates.bottomSalary.astype("int")
df_duplicates['avgSalary'] = df_duplicates.apply(lambda x:(x.bottomSalary+x.topSalary)/2,axis=1)

df_clean = df_duplicates[['city','companyShortName','companySize','education','positionName','positionLables','workYear','avgSalary']]
df_clean.head()

df_clean.city.value_counts()

df_clean.describe()

%matplotlib inline # jupyter自带的方式
plt.style.use('ggplot')
# df_clean.avgSalary.hist()
df_clean.avgSalary.hist(bins=15)

# df_clean.boxplot(column='avgSalary',by='city',figsize=(9,7))
font_zh = FontProperties(fname="d:/数据分析/simsun.ttc")
ax = df_clean.boxplot(column='avgSalary',by='city',figsize=(9,7))
for label in ax.get_xticklabels():
    label.set_fontproperties(font_zh)

ax = df_clean.boxplot(column='avgSalary',by='education',figsize=(9,7))
for label in ax.get_xticklabels():
    label.set_fontproperties(font_zh)

df_clean.sort_values('workYear')
ax = df_clean.boxplot(column='avgSalary',by='workYear',figsize=(9,7))
for label in ax.get_xticklabels():
    label.set_fontproperties(font_zh)

df_sh_bj = df_clean[df_clean['city'].isin(['上海','北京'])]
ax = df_clean.boxplot(column='avgSalary',by=['education','city'],figsize=(14,6))
for label in ax.get_xticklabels():
    label.set_fontproperties(font_zh)