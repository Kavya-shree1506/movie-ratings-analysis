
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("movie_ratings.csv")

# Display dataset
print("\nMOVIE RATINGS ANALYSIS")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Average rating
average_rating = df["rating"].mean()
print("\nAverage Movie Rating:", round(average_rating, 2))

# Highest rated movie
top_movie = df.loc[df["rating"].idxmax()]
print("\nHighest Rated Movie:")
print(top_movie["movie_title"], "-", top_movie["rating"])

# Top 5 movies
print("\nTop 5 Movies:")
print(df.nlargest(5, "rating")[["movie_title", "rating"]])

# Genre-wise average rating
genre_ratings = df.groupby("genre")["rating"].mean()
print("\nGenre-wise Average Ratings:")
print(genre_ratings)

# Genre-wise visualization
genre_ratings.plot(kind="bar", title="Average Rating by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()

# Top 5 movies visualization
top5 = df.nlargest(5, "rating")
plt.bar(top5["movie_title"], top5["rating"])
plt.title("Top 5 Highest Rated Movies")
plt.xlabel("Movie")
plt.ylabel("Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

