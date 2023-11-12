import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
a = pd.read_excel("C:\\Users\\guin22\\Desktop\\大数据分析（B）第一次作业——方差分析\\data.xlsx")  # 请注意这里我用的是绝对路径
b=list(a.values[:,6])  # 将第七列的数据转化为列表

fig = plt.figure(figsize=(10, 6))
plt.title('Scatter plot of the average age data')
for i in range(len(b)):
    plt.scatter(i, b[i])
plt.grid()
plt.show()


# 绘制直方图
plt.figure(figsize=(10, 6))
plt.title('Histogram of the average age data')
plt.hist(x=b,bins=int(len(b)/13), alpha=0.5,label='直方图')
plt.grid()
plt.show()


# 绘制密度图
data = pd.Series(b)
plt.title('Density plot of the average age data')
data.plot(kind='kde', secondary_y=True, label='密度图',color='red')
plt.grid()  # 添加网格
plt.show()


s = pd.DataFrame(b,columns=['value'])
u = s['value'].mean()
std = s['value'].std()  # 计算标准差
print('scipy.stats.kstest统计检验结果：----------------------------------------------------')
print(scipy.stats.kstest(s['value'], 'norm', (u, std)))
print('scipy.stats.normaltest统计检验结果：----------------------------------------------------')
print(scipy.stats.normaltest(s['value']))
print('scipy.stats.shapiro统计检验结果：----------------------------------------------------')
print(scipy.stats.shapiro(s['value']))

