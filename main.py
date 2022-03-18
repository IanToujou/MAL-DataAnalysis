import pandas as pd

anime_data = pd.read_csv('data/anime_cleaned.csv', na_values=r'\N')
print(anime_data)
