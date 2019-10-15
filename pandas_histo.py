import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/journeys.csv.gz")

plt.figure()
hist = df.hist(column = "Start Hour", bins = 24)

plt.title("Start Hours")
plt.xlabel("Hour")
plt.ylabel("Count")
plt.show()
