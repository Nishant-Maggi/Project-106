import csv
import plotly.express as px
import pandas as pd 
import numpy as np 

with open("collegeMarks.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)
    file_data.pop(0)
    marks = []
    present_days = []

    for i in file_data:
        marks.append(float(i[1]))
        present_days.append(float(i[2]))

    corelation = np.corrcoef(marks, present_days)
    print(corelation[0, 1])
    df = pd.read_csv("collegeMarks.csv")
    sc = px.scatter(df, x = "Marks In Percentage", y = "Days Present")
    sc.show()