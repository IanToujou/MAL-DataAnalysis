import pandas as pd
import matplotlib as matplotlib
import matplotlib.pyplot as plt

anime_data = pd.read_csv("data/anime_cleaned.csv", na_values=r'\N')

top_anime = anime_data.sort_values(by="rank", ascending=True)
top_anime_cleaned = top_anime.head(10)
top_anime_cleaned.plot(x="title", y="rank", kind="bar", rot=30, fontsize=10, color="purple")

plt.show()