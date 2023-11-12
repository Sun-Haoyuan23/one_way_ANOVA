import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
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


#检验类别1
s1 = pd.DataFrame(b1,columns=['value1'])
u = s1['value1'].mean()
std = s1['value1'].std()  # 计算标准差
print('这是对s1的检验')
print('scipy.stats.kstest统计检验结果：----------------------------------------------------')
print(scipy.stats.kstest(s1['value1'], 'norm', (u, std)))
print('scipy.stats.normaltest统计检验结果：----------------------------------------------------')
print(scipy.stats.normaltest(s1['value1']))
print('scipy.stats.shapiro统计检验结果：----------------------------------------------------')
print(scipy.stats.shapiro(s1['value1']))

#检验类别2
s2 = pd.DataFrame(b2,columns=['value2'])
u = s2['value2'].mean()
std = s2['value2'].std()  # 计算标准差
print('这是对s2的检验')
print('scipy.stats.kstest统计检验结果：----------------------------------------------------')
print(scipy.stats.kstest(s2['value2'], 'norm', (u, std)))
print('scipy.stats.normaltest统计检验结果：----------------------------------------------------')
print(scipy.stats.normaltest(s2['value2']))
print('scipy.stats.shapiro统计检验结果：----------------------------------------------------')
print(scipy.stats.shapiro(s2['value2']))

#检验类别3
s3 = pd.DataFrame(b3,columns=['value3'])
u = s3['value3'].mean()
std = s3['value3'].std()  # 计算标准差
print('这是对s3的检验')
print('scipy.stats.kstest统计检验结果：----------------------------------------------------')
print(scipy.stats.kstest(s3['value3'], 'norm', (u, std)))
print('scipy.stats.normaltest统计检验结果：----------------------------------------------------')
print(scipy.stats.normaltest(s3['value3']))
print('scipy.stats.shapiro统计检验结果：----------------------------------------------------')
print(scipy.stats.shapiro(s3['value3']))

#检验类别4
s4 = pd.DataFrame(b4,columns=['value4'])
u = s4['value4'].mean()
std = s4['value4'].std()  # 计算标准差
print('这是对s4的检验')
print('scipy.stats.kstest统计检验结果：----------------------------------------------------')
print(scipy.stats.kstest(s4['value4'], 'norm', (u, std)))
print('scipy.stats.normaltest统计检验结果：----------------------------------------------------')
print(scipy.stats.normaltest(s4['value4']))
print('scipy.stats.shapiro统计检验结果：----------------------------------------------------')
print(scipy.stats.shapiro(s4['value4']))

#检验类别5
s5 = pd.DataFrame(b5,columns=['value5'])
u = s5['value5'].mean()
std = s5['value5'].std()  # 计算标准差
print('这是对s5的检验')
print('scipy.stats.kstest统计检验结果：----------------------------------------------------')
print(scipy.stats.kstest(s5['value5'], 'norm', (u, std)))
print('scipy.stats.normaltest统计检验结果：----------------------------------------------------')
print(scipy.stats.normaltest(s5['value5']))
print('scipy.stats.shapiro统计检验结果：----------------------------------------------------')
print(scipy.stats.shapiro(s5['value5']))


def group_mean(group_list):
    '''
    :param group_list: 各个组的列表
    :return: 各个组的均值
    '''
    Sum = 0
    for i in range(len(group_list)):
        Sum += group_list[i]
    return Sum / (len(group_list))


def within_group_var(grand_group_list):
    '''
    求解组内的方差之和
    :param grand_group_list: 每一个组的数据是一个列表，全部的组最终组成一个列表
    :return: SSW
    '''
    SSW = 0
    a = group_mean(grand_group_list)  # 求出组内的均值
    for i in range(len(grand_group_list)):
        SSW += (grand_group_list[i] - a) ** 2
        pass
    return SSW

def within_group_var_mean(grand_group_list):
    '''
    方差：组内方差之和除以自由度
    :param grand_group_list:
    :return:
    '''
    SSW=within_group_var(grand_group_list)
    df=len(grand_group_list)-1
    return SSW/df

SSW_mean1=within_group_var_mean(b1)
print('第一部分的方差为{}'.format(SSW_mean1))

SSW_mean2=within_group_var_mean(b2)
print('第二部分的方差为{}'.format(SSW_mean2))

SSW_mean3=within_group_var_mean(b3)
print('第三部分的方差为{}'.format(SSW_mean3))

SSW_mean4=within_group_var_mean(b4)
print('第四部分的方差为{}'.format(SSW_mean4))

SSW_mean5=within_group_var_mean(b5)
print('第五部分的方差为{}'.format(SSW_mean5))

print('方差的最大值为{}，方差的最小值为{}'.format(max(SSW_mean1,SSW_mean2,SSW_mean3,SSW_mean4,SSW_mean5),min((SSW_mean1,SSW_mean2,SSW_mean3,SSW_mean4,SSW_mean5))))
print('比值为{}'.format(max(SSW_mean1,SSW_mean2,SSW_mean3,SSW_mean4,SSW_mean5)/min((SSW_mean1,SSW_mean2,SSW_mean3,SSW_mean4,SSW_mean5))))