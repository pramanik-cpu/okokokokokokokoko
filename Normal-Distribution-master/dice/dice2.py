import random
import plotly.figure_factory as pf

count=[]
dic_result=[]

for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dic_result.append(dice1+dice2)
    
fig = pf.create_distplot([dic_result], ["Result"]) 
fig.show()
