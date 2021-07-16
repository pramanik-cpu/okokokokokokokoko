import random
import plotly.express as px

count=[]
dic_result=[]
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dic_result.append(dice1,dice2)
    count.append(i)

print(count,dic_result)

fig=px.bar(x=dic_result,y=count)
fig.show()

