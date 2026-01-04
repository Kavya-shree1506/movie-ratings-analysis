import pandas as pd

# 1️⃣ Load the dataset
df = pd.read_csv("data/movies.csv")

# 2️⃣ Basic info
print("🔹 Dataset Info:")
print(df.info())

print("\n🔹 First 5 Rows:")
print(df.head())

# 3️⃣ Handle missing values
df.dropna(inplace=True)

# 4️⃣ Overall average rating
avg_rating = df["rating"].mean()
print(f"\n⭐ Average Movie Rating: {avg_rating:.2f}")

# 5️⃣ Top 5 highest-rated movies
top_movies = df.sort_values(by="rating", ascending=False).head(5)
print("\n🏆 Top 5 Highest Rated Movies:")
print(top_movies[["title", "rating"]])  # Fixed column name

# 6️⃣ Genre-wise average rating
genre_avg = df.groupby("genre")["rating"].mean().sort_values(ascending=False)
print("\n🎭 Average Rating by Genre:")
print(genre_avg)

# 7️⃣ Movies released per year
movies_per_year = df["year"].value_counts().sort_index()
print("\n📅 Movies Released Per Year:")
print(movies_per_year)

# 8️⃣ Save results to CSV
genre_avg.to_csv("genre_wise_average_rating.csv")
top_movies.to_csv("top_rated_movies.csv", index=False)

print("\n✅ Analysis Completed. Results saved successfully!")


