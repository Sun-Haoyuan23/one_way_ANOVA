import numpy as np
import pandas as pd
import math
import scipy
import matplotlib.pyplot as plt

a = pd.read_excel("C:\\Users\\guin22\\Desktop\\大数据分析（B）第一次作业——方差分析\\data.xlsx")  # 请注意这里我用的是绝对路径


class test_of_ANOVA:
    def __init__(self, listb, listc):
        b1 = []
        for i in range(len(listc)):
            if listc[i] == 1:
                b1.append(listb[i])  # 这里将第二列的数值为1的单独拿出来组成一个列表，下面同理

        b2 = []
        for i in range(len(listc)):
            if listc[i] == 2:
                b2.append(listb[i])

        b3 = []
        for i in range(len(listc)):
            if listc[i] == 3:
                b3.append(listb[i])

        b4 = []
        for i in range(len(listc)):
            if listc[i] == 4:
                b4.append(listb[i])

        b5 = []
        for i in range(len(listc)):
            if listc[i] == 5:
                b5.append(listb[i])
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5

    def test_col(self, grand_group, num):
        '''
        这是对整列数据的检验
        :param grand_group: 整个列的全体组成的列表
        :param num: 第几列
        :return:
        '''
        s = pd.DataFrame(grand_group, columns=['value'])
        u = s['value'].mean()
        std = s['value'].std()  # 计算标准差
        print('scipy.stats.kstest统计检验结果：----------------------------------------------------')
        print(scipy.stats.kstest(s['value'], 'norm', (u, std)))
        print('scipy.stats.normaltest统计检验结果：----------------------------------------------------')
        print(scipy.stats.normaltest(s['value']))
        print('scipy.stats.shapiro统计检验结果：----------------------------------------------------')
        print(scipy.stats.shapiro(s['value']))
        # 画出密度图
        data = pd.Series(grand_group)
        plt.title('Density plot of the average age data for column {}'.format(num))
        data.plot(kind='kde', secondary_y=True, label='密度图', color='red')
        plt.grid()  # 添加网格
        plt.show()

    def test_col1(self):
        s1 = pd.DataFrame(self.b1, columns=['value1'])
        u = s1['value1'].mean()
        std = s1['value1'].std()  # 计算标准差
        print('这是对s1的检验')
        print('scipy.stats.kstest统计检验结果：----------------------------------------------------')
        print(scipy.stats.kstest(s1['value1'], 'norm', (u, std)))
        print('scipy.stats.normaltest统计检验结果：----------------------------------------------------')
        print(scipy.stats.normaltest(s1['value1']))
        print('scipy.stats.shapiro统计检验结果：----------------------------------------------------')
        print(scipy.stats.shapiro(s1['value1']))

    def test_col2(self):
        s2 = pd.DataFrame(self.b2, columns=['value2'])
        u = s2['value2'].mean()
        std = s2['value2'].std()  # 计算标准差
        print('这是对s2的检验')
        print('scipy.stats.kstest统计检验结果：----------------------------------------------------')
        print(scipy.stats.kstest(s2['value2'], 'norm', (u, std)))
        print('scipy.stats.normaltest统计检验结果：----------------------------------------------------')
        print(scipy.stats.normaltest(s2['value2']))
        print('scipy.stats.shapiro统计检验结果：----------------------------------------------------')
        print(scipy.stats.shapiro(s2['value2']))

    def test_col3(self):
        s3 = pd.DataFrame(self.b3, columns=['value3'])
        u = s3['value3'].mean()
        std = s3['value3'].std()  # 计算标准差
        print('这是对s3的检验')
        print('scipy.stats.kstest统计检验结果：----------------------------------------------------')
        print(scipy.stats.kstest(s3['value3'], 'norm', (u, std)))
        print('scipy.stats.normaltest统计检验结果：----------------------------------------------------')
        print(scipy.stats.normaltest(s3['value3']))
        print('scipy.stats.shapiro统计检验结果：----------------------------------------------------')
        print(scipy.stats.shapiro(s3['value3']))

    def test_col4(self):
        s4 = pd.DataFrame(self.b4, columns=['value4'])
        u = s4['value4'].mean()
        std = s4['value4'].std()  # 计算标准差
        print('这是对s4的检验')
        print('scipy.stats.kstest统计检验结果：----------------------------------------------------')
        print(scipy.stats.kstest(s4['value4'], 'norm', (u, std)))
        print('scipy.stats.normaltest统计检验结果：----------------------------------------------------')
        print(scipy.stats.normaltest(s4['value4']))
        print('scipy.stats.shapiro统计检验结果：----------------------------------------------------')
        print(scipy.stats.shapiro(s4['value4']))

    def test_col5(self):
        s5 = pd.DataFrame(self.b5, columns=['value5'])
        u = s5['value5'].mean()
        std = s5['value5'].std()  # 计算标准差
        print('这是对s5的检验')
        print('scipy.stats.kstest统计检验结果：----------------------------------------------------')
        print(scipy.stats.kstest(s5['value5'], 'norm', (u, std)))
        print('scipy.stats.normaltest统计检验结果：----------------------------------------------------')
        print(scipy.stats.normaltest(s5['value5']))
        print('scipy.stats.shapiro统计检验结果：----------------------------------------------------')
        print(scipy.stats.shapiro(s5['value5']))

    def log_trans(self,grand_list,bias):
        '''
        对数变换
        :param grand_list: 要变换数据的列表
        :param bias: 偏置项，避免真数为0
        :return: 变换后数据的列表
        '''
        log_trans_list=[]
        for i in grand_list:
            a=math.log(i+bias)
            log_trans_list.append(a)
        return log_trans_list

    def exp_trans(self,grand_list):
        '''
        指数变换
        :param grand_list: 要变换数据的列表
        :return: 变换后数据的列表
        '''
        exp_trans_list=[]
        for i in grand_list:
            i=float(i)
            a = math.exp(i)
            exp_trans_list.append(a)
        return exp_trans_list
    def sqrt_trans(self,grand_list):
        '''
        平方根变换
        :param grand_list: 要变换数据的列表
        :return: 变换后数据的列表
        '''
        sqrt_trans_list = []
        for i in grand_list:
            i = float(i)
            a = math.sqrt(i)
            sqrt_trans_list.append(a)
        return sqrt_trans_list

    def group_mean(self, group_list):
        '''
        :param group_list: 各个组的列表
        :return: 各个组的均值
        '''
        Sum = 0
        for i in range(len(group_list)):
            Sum += group_list[i]
        return Sum / (len(group_list))

    def within_group_var(self, grand_group_list):
        '''
        求解组内的方差之和
        :param grand_group_list: 每一个组的数据是一个列表，全部的组最终组成一个列表
        :return: SSW
        '''
        SSW = 0
        a = self.group_mean(grand_group_list)  # 求出组内的均值
        for i in range(len(grand_group_list)):
            SSW += (grand_group_list[i] - a) ** 2
            pass
        return SSW

    def within_group_var_mean(self, grand_group_list):
        '''
        方差：组内方差之和除以自由度
        :param grand_group_list:
        :return:
        '''
        SSW = self.within_group_var(grand_group_list)
        df = len(grand_group_list) - 1
        return SSW / df

    def output(self):
        SSW_mean1 = self.within_group_var_mean(self.b1)
        print('第一部分的方差为{}'.format(SSW_mean1))

        SSW_mean2 = self.within_group_var_mean(self.b2)
        print('第二部分的方差为{}'.format(SSW_mean2))

        SSW_mean3 = self.within_group_var_mean(self.b3)
        print('第三部分的方差为{}'.format(SSW_mean3))

        SSW_mean4 = self.within_group_var_mean(self.b4)
        print('第四部分的方差为{}'.format(SSW_mean4))

        SSW_mean5 = self.within_group_var_mean(self.b5)
        print('第五部分的方差为{}'.format(SSW_mean5))

        print('方差的最大值为{}，方差的最小值为{}'.format(max(SSW_mean1, SSW_mean2, SSW_mean3, SSW_mean4, SSW_mean5),
                                                         min((SSW_mean1, SSW_mean2, SSW_mean3, SSW_mean4, SSW_mean5))))
        print('比值为{}'.format(
            max(SSW_mean1, SSW_mean2, SSW_mean3, SSW_mean4, SSW_mean5) / min(SSW_mean1, SSW_mean2, SSW_mean3, SSW_mean4,
                                                                             SSW_mean5)))


# 测试第三列数据
print('这是对第三列数据的检验')
b = list(a.values[:, 2])  # 将第三列的数据转化为列表
c = list(a.values[:, 1])  # 这里取出第二列的全部数据
test_of_ANOVA_col3=test_of_ANOVA(b,c)
test_of_ANOVA_col3.test_col(b,3)
test_of_ANOVA_col3.output()

# 将第三列数据对数变换，并进行检验
print('这是对第三列数据对数变换后的检验')
b_log=test_of_ANOVA_col3.log_trans(b,1)
test_of_ANOVA_col3=test_of_ANOVA(b_log,c)
test_of_ANOVA_col3.test_col(b_log,3)
test_of_ANOVA_col3.output()

# 测试第四列数据
print('这是对第四列数据的检验')
b = list(a.values[:, 3])  # 将第四列的数据转化为列表
c = list(a.values[:, 1])  # 这里取出第二列的全部数据
test_of_ANOVA_col4=test_of_ANOVA(b,c)
test_of_ANOVA_col4.test_col(b,4)
test_of_ANOVA_col4.output()

# 将第四列数据对数变换，并进行检验
print('这是对第四列数据对数变换后的检验')
b_log=test_of_ANOVA_col4.log_trans(b,1e-2)
test_of_ANOVA_col4=test_of_ANOVA(b_log,c)
test_of_ANOVA_col4.test_col(b_log,4)
test_of_ANOVA_col4.output()

# 测试第八列数据
print('这是对第八列数据的检验')
b = list(a.values[:, 7])  # 将第八列的数据转化为列表
c = list(a.values[:, 1])  # 这里取出第二列的全部数据
test_of_ANOVA_col8=test_of_ANOVA(b,c)
test_of_ANOVA_col8.test_col(b,8)
test_of_ANOVA_col8.output()

# 将第八列数据对数变换，并进行检验
print('这是对第八列数据对数变换后的检验')
b_log=test_of_ANOVA_col8.log_trans(b,1e-5)
test_of_ANOVA_col8=test_of_ANOVA(b_log,c)
test_of_ANOVA_col8.test_col(b_log,8)
test_of_ANOVA_col8.output()
