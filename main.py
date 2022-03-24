import pandas as pd
import matplotlib as matplotlib
import matplotlib.pyplot as plt

# Set plot settings
dpi = 82

# Get the data frm the CSV files.
anime_data = pd.read_csv("data/anime_cleaned.csv", na_values=r'\N')

# What are the top 10 anime sorted by member count?
top_anime = anime_data.sort_values(by="members", ascending=False)
top_anime_cleaned = top_anime.head(10)
top_anime_cleaned.plot(x="title", y="members", kind="bar", rot=30, fontsize=12, color="green")
plt.show()

# What are the top 10 hentai sorted by member count?
top_hentai = top_anime[top_anime.rating=="Rx - Hentai"].sort_values(by="members", ascending=False)
top_hentai_cleaned = top_hentai.head(10)
top_hentai_cleaned.plot(x="title", y="members", kind="bar", rot=30, fontsize=12, color="orange")
plt.show()

# What is the anime with the most episodes?
most_episodes = anime_data.sort_values(by="episodes", ascending=False)
most_episodes_cleaned = most_episodes.head(10)
most_episodes_cleaned.plot(x="title", y="episodes", kind="bar", rot=30, fontsize=12, color="purple")
plt.show()