import csv
import plotly.express as px
import pandas as pd 
import numpy as np 

with open("coffeeSleep.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)
    file_data.pop(0)
    coffee = []
    sleep = []

    for i in file_data:
        coffee.append(float(i[1]))
        sleep.append(float(i[2]))

    corelation = np.corrcoef(coffee, sleep)
    print(corelation[0, 1])
    df = pd.read_csv("coffeeSleep.csv")
    sc = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
    sc.show()