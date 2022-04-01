import pandas as pd
import matplotlib as matplotlib
import matplotlib.pyplot as plt

# Set plot settings
dpi = 82

# Get the data frm the CSV files.
anime_data = pd.read_csv("data/anime_cleaned.csv", na_values=r'\N')
user_data = pd.read_csv("data/users_cleaned.csv", na_values=r'\N')
waifu_data = pd.read_csv("data/waifus_cleaned.csv", na_values=r'\N')

# Biggest booba size
top_waifus = waifu_data.sort_values(by="bust", ascending=False)
top_waifus = top_waifus[top_waifus.bust < 1000].head(10)
top_waifus.plot(x="name", y="bust", kind="bar", rot=30, fontsize=12, color="blue")
plt.show()

# What are the top 10 anime sorted by member count?
top_anime = anime_data.sort_values(by="members", ascending=False)
top_anime_cleaned = top_anime.head(10)
top_anime_cleaned.plot(x="title", y="members", kind="bar", rot=30, fontsize=12, color="green")
plt.show()

# What are the top 10 anime by age rating?
top_hentai = top_anime[top_anime.rating=="Rx - Hentai"].sort_values(by="members", ascending=False)
top_hentai_cleaned = top_hentai.head(10)
top_hentai_cleaned.plot(x="title", y="members", kind="bar", rot=30, fontsize=12, color="orange")
plt.show()

# What is the anime with the most episodes?
most_episodes = anime_data.sort_values(by="episodes", ascending=False)
most_episodes_cleaned = most_episodes.head(10)
most_episodes_cleaned.plot(x="title", y="episodes", kind="bar", rot=30, fontsize=12, color="purple")
plt.show()

# Top genders in user date
male_users = user_data[user_data.gender=="Male"]
female_users = user_data[user_data.gender=="Female"]
genders = ["Male", "Female"]
male_count = male_users["username"].count()
female_count = female_users["username"].count()
gender_data = [male_count, female_count]
plt.pie(gender_data, labels=genders)
plt.show()

top_watchers = user_data.sort_values(by="user_days_spent_watching", ascending=False)
top_watchers_cleaned = top_watchers.head(10)
top_watchers_cleaned.plot(x="username", y="user_days_spent_watching", kind="bar", rot=30, fontsize=12, color="blue")
plt.show()