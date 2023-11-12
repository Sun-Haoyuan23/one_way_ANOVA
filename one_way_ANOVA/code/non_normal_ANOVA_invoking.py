# 在本代码中，调用scipy.stats.f_oneway库实现单因素方差分析
import scipy.stats as stats
import pandas as pd
import math
a = pd.read_excel("C:\\Users\\guin22\\Desktop\\大数据分析（B）第一次作业——方差分析\\data.xlsx")  # 请注意这里我用的是绝对路径,用pandas库读取文件
#C3-C2
b=list(a.values[:,2])  # 这里取出第三列的全部数据
c=list(a.values[:,1])  # 这里取出第二列的全部数据

b1=[]
for i in range(len(c)):
    if c[i]==1:
        b[i]=math.log(b[i])
        b1.append(b[i])  # 这里将第二列的数值为1的单独拿出来,经过对数变换，组成一个列表，下面同理

b2=[]
for i in range(len(c)):
    if c[i]==2:
        b[i] = math.log(b[i])
        b2.append(b[i])

b3=[]
for i in range(len(c)):
    if c[i]==3:
        b[i] = math.log(b[i])
        b3.append(b[i])

b4=[]
for i in range(len(c)):
    if c[i]==4:
        b[i] = math.log(b[i])
        b4.append(b[i])

b5=[]
for i in range(len(c)):
    if c[i]==5:
        b[i] = math.log(b[i])
        b5.append(b[i])


## perform one-way ANOVA
f_value, p_value = stats.f_oneway(b1,b2,b3,b4,b5)

## print the result
print('result of C3-C2 is as follows')
print("F-value:", f_value)
print("P-value:", p_value)

#C4-C2
b=list(a.values[:,3])  # 这里取出第四列的全部数据
c=list(a.values[:,1])  # 这里取出第二列的全部数据

b1=[]
for i in range(len(c)):
    if c[i]==1:
        b[i]=math.log(b[i])
        b1.append(b[i])  # 这里将第二列的数值为1的单独拿出来,经过对数变换，组成一个列表，下面同理

b2=[]
for i in range(len(c)):
    if c[i]==2:
        b[i] = math.log(b[i])
        b2.append(b[i])

b3=[]
for i in range(len(c)):
    if c[i]==3:
        b[i] = math.log(b[i])
        b3.append(b[i])

b4=[]
for i in range(len(c)):
    if c[i]==4:
        b[i] = math.log(b[i])
        b4.append(b[i])

b5=[]
for i in range(len(c)):
    if c[i]==5:
        b[i] = math.log(b[i])
        b5.append(b[i])


## perform one-way ANOVA
f_value, p_value = stats.f_oneway(b1,b2,b3,b4,b5)

## print the result
print('result of C4-C2 is as follows')
print("F-value:", f_value)
print("P-value:", p_value)

#C8-C2
b=list(a.values[:,7])  # 这里取出第八列的全部数据
c=list(a.values[:,1])  # 这里取出第二列的全部数据

b1=[]
for i in range(len(c)):
    if c[i]==1:
        b1.append(b[i])  # 这里将第二列的数值为1的单独拿出来,经过对数变换，组成一个列表，下面同理

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
f_value, p_value = stats.f_oneway(b1,b2,b3,b4,b5)

## print the result
print('result of C8-C2 is as follows')
print("F-value:", f_value)
print("P-value:", p_value)

#C3-C4-C8
b=list(a.values[:,2])  # 这里取出第三列的全部数据
c=list(a.values[:,3])  # 这里取出第四列的全部数据
d=list(a.values[:,7])  # 这里取出第八列的全部数据
def log_trans(grand_list, bias):
    '''
    对数变换
    :param grand_list: 要变换数据的列表
    :param bias: 偏置项，避免真数为0
    :return: 变换后数据的列表
    '''
    log_trans_list = []
    for i in grand_list:
        a = math.log(i + bias)
        log_trans_list.append(a)
    return log_trans_list
b1=log_trans(b,1e-2)
c1=log_trans(c,1e-2)

## perform one-way ANOVA
f_value, p_value = stats.f_oneway(b1,c1,d)

# ## print the result
print('result of C3-C4-C8 is as follows')
print("F-value:", f_value)
print("P-value:", p_value)


#C3-C4
## perform one-way ANOVA
f_value, p_value = stats.f_oneway(b1,c1)

## print the result
print('result of C3-C4 is as follows')
print("F-value:", f_value)
print("P-value:", p_value)


#C3-C8
## perform one-way ANOVA
f_value, p_value = stats.f_oneway(b1,d)

## print the result
print('result of C3-C8 is as follows')
print("F-value:", f_value)
print("P-value:", p_value)


#C4-C8
## perform one-way ANOVA
f_value, p_value = stats.f_oneway(c1,d)

# ## print the result
print('result of C4-C8 is as follows')
print("F-value:", f_value)
print("P-value:", p_value)