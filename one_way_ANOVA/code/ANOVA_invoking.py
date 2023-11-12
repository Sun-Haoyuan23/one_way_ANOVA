# 在本代码中，调用scipy.stats.f_oneway库实现单因素方差分析
import scipy.stats as stats
import pandas as pd
a = pd.read_excel("C:\\Users\\guin22\\Desktop\\大数据分析（B）第一次作业——方差分析\\data.xlsx")  # 请注意这里我用的是绝对路径,用pandas库读取文件
b=list(a.values[:,6])  # 这里取出第七列的全部数据
c=list(a.values[:,1])  # 这里取出第二列的全部数据

b1=[]
for i in range(len(c)):
    if c[i]==1:
        b1.append(b[i])  # 这里将第二列的数值为1的单独拿出来组成一个列表，下面同理

b2=[]
for i in range(len(c)):
    if c[i]==2:
        b2.append(b[i])

b3=[]
for i in range(len(c)):
    if c[i]==3:
        b3.append(b[i])

b4=[]
for i in range(len(c)):
    if c[i]==4:
        b4.append(b[i])

b5=[]
for i in range(len(c)):
    if c[i]==5:
        b5.append(b[i])

## perform one-way ANOVA
f_value, p_value = stats.f_oneway(b1, b2, b3,b4,b5)

## print the result
print("F-value:", f_value)
print("P-value:", p_value)