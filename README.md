🎬 Movie Ratings Analysis

A beginner-to-intermediate Python data analysis project using Pandas to analyze movie ratings from a CSV dataset.

This project demonstrates a complete data analysis workflow including data loading, cleaning, aggregation, and exporting results — built using VS Code and hosted on GitHub.

📂 Project Structure
movie-ratings-analysis/
├── data/
│   └── movies.csv
├── analysis.py
├── genre_wise_average_rating.csv
├── top_rated_movies.csv
├── requirements.txt
└── README.md

🛠 Tools & Libraries

Python 3.x

Pandas

VS Code

Git & GitHub

📊 Dataset Details

The dataset movies.csv contains the following columns:

Column	Description
movie_id	Unique ID for each movie
title	Movie title
genre	Movie genre
rating	Movie rating (float)
year	Release year
✨ What This Project Does

Based on the code in analysis.py, this project performs:

Loads the dataset using Pandas

Displays dataset info & first 5 rows

Handles missing values by removing null rows

Calculates overall average movie rating

Finds top 5 highest-rated movies

Computes genre-wise average ratings

Counts movies released per year

Exports results to CSV files

🚀 How to Run the Project
# Clone the repository
git clone https://github.com/Kavya-shree1506/movie-ratings-analysis.git

# Navigate to project folder
cd movie-ratings-analysis

# Install dependencies
pip install -r requirements.txt

# Run the analysis
python analysis.py

📁 Output Files Generated

After running the script, the following files are created:

top_rated_movies.csv → Top 5 highest-rated movies

genre_wise_average_rating.csv → Average rating per genre

🧠 Sample Insights

Overall average movie rating is calculated

Top-rated movies are identified

Genre-wise rating trends are analyzed

Movie release patterns by year are observed

📌 Author

Kavya Shree R.S
B.Sc Data Analytics student
Building hands-on Python & data analytics projects 🚀

✅ GitHub Ready Checklist

✔ README matches the code
✔ Clean project structure
✔ Beginner-friendly & recruiter-friendly
