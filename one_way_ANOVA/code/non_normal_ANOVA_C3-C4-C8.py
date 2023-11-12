import pandas as pd
import matplotlib.pyplot as plt
import math


class ANOVA_Single:
    def __init__(self):
        pass

    def grand_mean(self, grand_list):
        '''
        :param grand_list: 全体的列表
        :return: 整体的均值
        '''
        Sum = 0
        for i in grand_list:
            Sum += i
        return Sum / (len(grand_list))

    def group_mean(self, group_list):
        '''
        :param group_list: 各个组的列表
        :return: 各个组的均值
        '''
        Sum = 0
        for i in group_list:
            Sum += i
        return Sum / (len(group_list))

    def within_group_var(self, grand_group_list):
        '''
        求解组内的方差之和
        :param grand_group_list: 每一个组的数据是一个列表，全部的组最终组成一个列表
        :return: SSW
        '''
        SSW = 0
        for i in range(len(grand_group_list)):
            a = self.group_mean(grand_group_list[i])  # 求出组内的均值
            for j in range(len(grand_group_list[i])):
                SSW += (grand_group_list[i][j] - a) * (grand_group_list[i][j] - a)
                pass
            pass
        return SSW

    def between_group_var(self, grand_group_list):
        '''
        求解组间方差
        :param grand_group_list: 每一个组的数据是一个列表，全部的组最终组成一个列表
        :return: SSB
        '''
        length = len(grand_group_list)  # 共有多少组
        group_length_list = []
        for i in grand_group_list:
            group_length_list.append(len(i))  # 求出每一个组有多少元素，赋给group_length_list
            pass

        grand_list = []  # 把嵌套的列表改为只有一层的列表
        for i in range(len(grand_group_list)):
            for j in range(len(grand_group_list[i])):
                grand_list.append(grand_group_list[i][j])
                pass
            pass

        group_mean_list = []  # 求出每一个组的均值的列表
        for i in range(len(grand_group_list)):
            a = self.group_mean(grand_group_list[i])
            group_mean_list.append(a)
            pass

        grand_mean = self.grand_mean(grand_list)  # 求出总体的均值

        SSB = 0
        for k in range(length):
            SSB += group_length_list[k] * (group_mean_list[k] - grand_mean) * (group_mean_list[k] - grand_mean)
            pass

        return SSB

    def total_var(self, grand_group_list):
        '''
        求解总体方差，SSW与SSB之和
        :param grand_group_list: 每一个组的数据是一个列表，全部的组最终组成一个列表
        :return: 总体方差
        '''
        total_var = self.within_group_var(grand_group_list) + self.between_group_var(grand_group_list)
        return total_var

    def mean_between_group(self, grand_group_list):
        '''
        SSB除以自由度
        :param grand_group_list:
        :return: MSB
        '''
        df_between = len(grand_group_list) - 1
        SSB = self.between_group_var(grand_group_list)
        MSB = SSB / df_between
        return MSB

    def mean_within_group(self, grand_group_list):
        '''
        SSW除以自由度
        :param grand_group_list:
        :return: MSW
        '''
        grand_list = []
        for i in range(len(grand_group_list)):
            for j in range(len(grand_group_list[i])):
                grand_list.append(grand_group_list[i][j])
                pass
            pass
        n = len(grand_list)
        k = len(grand_group_list)
        df_within = n - k
        SSW = self.within_group_var(grand_group_list)
        MSW = SSW / df_within
        return MSW

    def F_statistic(self, grand_group_list):
        '''
        求出F值
        :param grand_group_list:
        :return: F值
        '''
        MSB = self.mean_between_group(grand_group_list)
        MSW = self.mean_within_group(grand_group_list)
        F = MSB / MSW
        return F

    def determine(self, grand_group_list):
        F = self.F_statistic(grand_group_list)
        df_between = len(grand_group_list) - 1
        grand_list = []
        for i in range(len(grand_group_list)):
            for j in range(len(grand_group_list[i])):
                grand_list.append(grand_group_list[i][j])
                pass
            pass
        n = len(grand_list)
        k = len(grand_group_list)
        df_within = n - k
        print('在这个情境下，得到的F值为{}，分子自由度是{}，分母自由度是{}'.format(F, df_between, df_within))
        # 判断
        a = float(input('请根据上述信息，查表得到α=0.05时F-crit的值'))
        if F >= a:
            print('With significance level of 5%,there is highly significant evidence to reject the null hypothesis')
            b = float(input('请根据上述信息，查表得到α=0.01时F-crit的值'))
            if F >= b:
                print(
                    'With significance level of 1%,there is highly significant evidence to reject the null hypothesis')
        else:
            print(
                'With significance level of 5%,there is no significant evidence to reject the null hypothesis,just keep the null hypothesis')
        pass

    pass


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


# 读取数据
a = pd.read_excel(
    "C:\\Users\\guin22\\Desktop\\大数据分析（B）第一次作业——方差分析\\data.xlsx")  # 请注意这里我用的是绝对路径,用pandas库读取文件
b = list(a.values[:, 2])  # 这里取出第三列的全部数据
c = list(a.values[:, 3])  # 这里取出第四列的全部数据
b1 = log_trans(b, 1e-2)
c1 = log_trans(c, 1e-2)
d = list(a.values[:, 7])  # 这里取出第八列的全部数据

e = [b1, c1, d]
ANOVA5 = ANOVA_Single()
ANOVA5.determine(e)
# 做出第三列、对数变换后的第三列、第四列、对数变换后的第四列、第八列的概率密度函数图
plt.figure(figsize=(15, 6))
data1 = pd.Series(b)
data2 = pd.Series(b1)
data3 = pd.Series(c)
data4 = pd.Series(c1)
data5 = pd.Series(d)
plt.title('Density plot')
plt.xlim((-5, 20))
plt.rcParams['font.sans-serif'] = ['KaiTi_GB2312']
data1.plot(kind='kde', secondary_y=True, color='red', label='第三列')
data2.plot(kind='kde', secondary_y=True, color='dodgerblue', label='对数变换后的第三列')
data3.plot(kind='kde', secondary_y=True, color='limegreen', label='第四列')
data4.plot(kind='kde', secondary_y=True, color='magenta', label='对数变换后的第四列')
data5.plot(kind='kde', secondary_y=True, color='indigo', label='第八列')
plt.legend()
plt.grid()  # 添加网格
plt.show()
