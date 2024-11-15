import pandas as pd

import numpy as np

import matplotlib.pyplot as plt



score=pd.read_excel(r"/home/zhouzhilin/2.预备知识/学生成绩.xlsx")

score=pd.DataFrame(score)



math=score[score['数学']>85]

print(math)



scoresorted=score.sort_values("英语",ascending=False)

print(scoresorted)



totalscore=score[["语文","数学","英语"]].sum(axis =1)
fig=plt.figure()
plt.scatter(range(totalscore.count()),totalscore,color='red')

plt.title("总分散点图",fontproperties='simhei')

plt.show()