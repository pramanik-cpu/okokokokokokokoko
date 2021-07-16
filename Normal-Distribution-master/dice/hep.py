from pandas.core.frame import DataFrame
import plotly.figure_factory as pf
import csv
import pandas as pd

df=pd.read_csv("data.csv")
fig = pf.create_distplot([df["Height(Inches)"].tolist()], ["Height"], show_hist=False)
fig.show()
