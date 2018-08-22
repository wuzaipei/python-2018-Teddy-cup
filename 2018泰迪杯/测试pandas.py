import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

data = pd.read_excel('./代码附件/附件一/电流电压/YD1.xlsx',sheet_name=1)
# print(data)
import numpy as np

x = Series(np.linspace(0,100,num=50))
x.cumsum().plot(title='DateFrom')
# plt.show()

df = DataFrame(np.random.randint(0,30,size=(10,4)),index=list('abcdefghij'),columns=list('ABCD'))

df.plot(title='DateFrom',kind='bar') # 列图
df.plot(title='DateFrom',kind='barh') # 水平


plt.show()