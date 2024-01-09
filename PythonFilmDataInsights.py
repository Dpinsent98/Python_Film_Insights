import pandas as pd
import numpy as np

films_stats = pd.read_csv("C:/Users/dragan/Desktop/FilmStats.csv")

print(films_stats.head())

print(films_stats.shape)

films_stats_clean = films_stats.dropna()

print(films_stats_clean.describe())

Mean_years = films_stats_clean.groupby("Year")["Gross"].mean()

Mean_years_df = Mean_years.reset_index()

Mean_years_df.columns = ["Year", "Mean_Gross"]

Mean_years_sorted = Mean_years_df.sort_values("Mean_Gross",ascending = False).head(1)

print(Mean_years_sorted)

Top_film = films_stats_clean.sort_values("Gross", ascending = False).head(1)

print(Top_film[["Top Movie","Gross","Year"]])

Top_5_genres = films_stats_clean.groupby("Genre")["Gross"].mean()

Top_5_genres_df = Top_5_genres.reset_index()

Top_5_genres_df.columns = ["Genre", "Mean_Gross"]

print(Top_5_genres_df.sort_values("Mean_Gross", ascending = False).head(5))


