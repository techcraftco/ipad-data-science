import numpy as np
import matplotlib.pyplot as plt

df = np.loadtxt('data/journeys.csv.gz', skiprows = 1, delimiter= ',')
start_hours = df[:,11]

plt.hist(start_hours, 24)
plt.title("Journey Start Hours")
plt.xlabel("Count")
plt.ylabel("Hour")
plt.show()