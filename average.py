from numpy import average
import plotly.figure_factory as ff
import random
import statistics
import csv
import plotly.graph_objects as pg
import pandas as pd

df = pd.read_csv('average.csv')
data = df["average"].tolist()
average_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("average mean",average_mean)
print("stdev",std_deviation)

def random_set_of_mean(counter):
    dataSet = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["average"],show_hist = False)
    fig.add_trace(pg.Scatter(x = [mean,mean],y = [0,1],mode = "lines",name = "MEAN"))
    fig.show()
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
    setup()


