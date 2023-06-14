import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("2023-06-13-survey.csv")

fig, ax = plt.subplots(1, 1)

ax = df["Hard Drive Size (in GB)"].hist(bins=50)
ax.set_xlabel("Hard Drive Size (GB)")
ax.set_ylabel("Count")
ax.set_ylim(0, 20)
plt.yticks(range(0, 20, 5))

fig.savefig("hist.png", dpi=150)