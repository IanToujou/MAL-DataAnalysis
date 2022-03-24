import pandas as pd
import matplotlib as matplotlib
import matplotlib.pyplot as plt

# Set plot settings
dpi = 82
plt.figure(figsize=(800/dpi, 800/dpi), dpi=dpi)

# Get the data frm the CSV files.
anime_data = pd.read_csv("data/anime_cleaned.csv", na_values=r'\N')

# What are the top 10 anime in general, sorted by member count?
top_anime = anime_data.sort_values(by="members", ascending=False)
top_anime_cleaned = top_anime.head(10)
top_anime_cleaned.plot(x="title", y="members", kind="bar", rot=90, fontsize=12, color="green")
plt.show()

# What are the top 10 hentai in general, sorted by member count?
top_hentai = top_anime[top_anime.rating=="Rx - Hentai"].sort_values(by="members", ascending=False)
top_hentai_cleaned = top_hentai.head(10)
top_hentai_cleaned.plot(x="title", y="members", kind="bar", rot=90, fontsize=12, color="orange")
plt.show()
