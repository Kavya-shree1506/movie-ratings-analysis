# 🎬 Movie Ratings Analysis

A beginner-to-intermediate **Python project** analyzing movie ratings using **Pandas**.  
The goal is to extract insights such as **top-rated movies**, **genre-wise rating trends**, and **movie release patterns** over the years.  

This project is perfect for practicing **data analysis workflows**, **Python scripting**, and **CSV handling**.

---

## 📂 Project Structure

movie-ratings-analysis/
├── data/
│ └── movies.csv # Dataset of movies
├── analysis.py # Python script
├── genre_wise_average_rating.csv # Output CSV (optional)
├── top_rated_movies.csv # Output CSV (optional)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 🛠 Tools & Libraries

- **Python 3.x**  
- **Pandas** – Data manipulation and analysis  
- **VS Code** – IDE  
- **Git & GitHub** – Version control and hosting  

---

## 🔹 Dataset

The dataset `movies.csv` includes:

| Column    | Description                     |
|----------|---------------------------------|
| movie_id | Unique ID for each movie        |
| title    | Movie title                     |
| genre    | Movie genre                     |
| rating   | Movie rating (IMDb-like, float) |
| year     | Release year                    |

**Sample Data:**

| movie_id | title             | genre     | rating | year |
|----------|-----------------|----------|--------|------|
| 1        | Inception        | Sci-Fi   | 8.8    | 2010 |
| 2        | Interstellar     | Sci-Fi   | 8.6    | 2014 |
| 3        | The Dark Knight  | Action   | 9.0    | 2008 |
| 4        | Parasite         | Thriller | 8.6    | 2019 |
| 5        | Avengers: Endgame| Action   | 8.4    | 2019 |

---

## 📊 Features

1. **Dataset Inspection** – View dataset info and first 5 rows  
2. **Handle Missing Values** – Drop rows with null values  
3. **Overall Average Rating** – Calculates mean rating for all movies  
4. **Top 5 Highest-Rated Movies** – Sorts movies by rating  
5. **Genre-Wise Average Rating** – Calculates average rating per genre  
6. **Movies Released Per Year** – Counts movies released each year  
7. **Save Results** – Outputs CSV files: `top_rated_movies.csv` and `genre_wise_average_rating.csv`

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/your-username/movie-ratings-analysis.git

# Go to project folder
cd movie-ratings-analysis

# Install dependencies
pip install -r requirements.txt

# Run the analysis
python analysis.py


Output files:

top_rated_movies.csv

genre_wise_average_rating.csv

🧠 Insights

Sci-Fi movies have the highest average rating

Top-rated movie: The Dark Knight (9.0)

Movie releases peaked after 2010

⭐ License

This project is open source and free to use for learning purposes.

📌 Author

Kavya – B.Sc Data Analytics student building practical Python projects.


---


