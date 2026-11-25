# 🎬 2024 Action Movie Recommender

An end-to-end data science project that scrapes the latest **2024 Action Movies** from IMDb and uses Natural Language Processing (NLP) to recommend films based on user-described "vibes" or plot points.

## 🚀 Features
* **Automated Web Scraping:** Utilizes Selenium to navigate IMDb’s dynamic JavaScript-loaded content and extract metadata for ~1,400+ titles.
* **Content-Based Filtering:** Employs TF-IDF Vectorization and Cosine Similarity to analyze semantic meaning in movie storylines.
* **Advanced Text Processing:** Uses N-grams (1,2) to capture both single words and meaningful phrases (e.g., "secret agent") for higher accuracy.
* **Modern UI:** A sleek, dark-themed dashboard built with Streamlit, featuring custom CSS and interactive movie "cards."
* **Data Integrity:** Includes a robust preprocessing pipeline to handle duplicates and missing values.

## 🛠️ Technology Stack
* **Language:** Python 3.10+
* **Scraping:** Selenium, WebDriver Manager
* **Data Science:** Pandas, Scikit-Learn
* **Web Framework:** Streamlit
* **Styling:** Custom CSS/HTML

## 📂 Project Structure
```text
├── webscrap.ipynb      # Part 1: Selenium script for data collection
├── recommender.py      # Part 2: NLP logic (TF-IDF + Cosine Similarity)
├── app.py              # Part 3: Streamlit User Interface
├── action_movies.csv   # Scraped dataset (1,400+ movie records)
└── requirement.txt     # List of required Python libraries

⚙️ How to Run
📊 Data Source
* **Target:** [IMDb Advanced Search (2024 Action Features)](https://www.imdb.com/search/title/?title_type=feature&release_date=2024-01-01,2024-12-31&genres=action&adult=include)
* **Scope:** This includes all feature-length action films released between January 1, 2024, and December 31, 2024.

1. Install dependencies:
Bash
pip install -r requirement.txt
2. Run the Application:
Bash
streamlit run app.py
🧠 Technical Overview
1. Data Acquisition & Cleaning
The project uses Selenium to scroll through IMDb's dynamic search results and click the "Load More" button automatically.

Deduplication: A cleaning phase in Pandas removes redundant entries caused by page-load glitches.

Validation: Entries lacking a storyline are filtered out to maintain the quality of the recommendation engine.

2. The Recommendation Engine
The model converts raw text into numerical vectors using TF-IDF.

N-grams: By setting the range to (1, 2), the model understands that "Special Forces" is more than just the word "Special."

Cosine Similarity: The app calculates the mathematical "distance" (angle) between your search query and every movie in the database, returning the 5 closest matches.

🔮 Future Enhancements
Movie Posters: Integrating a secondary scraper to fetch and display film posters in the UI.

Ratings Filter: Allowing users to filter recommendations based on IMDb star ratings.

Hybrid Model: Adding collaborative filtering based on user watch history.`
