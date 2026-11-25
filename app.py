import streamlit as st
import pandas as pd
from recommender import get_recommendations

# 1. Page Configuration
st.set_page_config(
    page_title="ActionStream 2024",
    page_icon="🎬",
    layout="wide"
)

# 2. Custom CSS for better UI
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #121212;
    }
    
    /* Title Styling */
    h1 {
        color: #FFD700 !important; /* Gold Color */
        font-family: 'Arial Black', sans-serif;
        text-align: center;
        text-transform: uppercase;
    }

    /* Change the color of the Label above the input box */
    .stTextInput label, .stTextArea label {
        color: #00FFC2 !important; /* Bright Neon Cyan */
        font-size: 18px !important;
        font-weight: bold !important;
    }

    /* Input Box styling */
    .stTextInput input {
        background-color: #262730 !important;
        color: white !important;
        border: 2px solid #00FFC2 !important;
    }

    /* Card Styling */
    .movie-card {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 12px;
        border-bottom: 4px solid #FFD700; /* Gold underline */
        margin-bottom: 25px;
        transition: 0.3s;
    }
    
    .movie-card:hover {
        background-color: #2d2d2d;
        transform: scale(1.01);
    }

    .movie-title {
        color: #FFD700 !important; /* Gold titles */
        font-size: 24px;
        font-weight: bold;
    }

    .movie-plot {
        color: #E0E0E0 !important; /* Brighter gray for story */
        font-size: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.title("🎬 ACTION STREAM 2024")
st.markdown("<p style='text-align: center; color: gray;'>AI-Powered Movie Discovery for Action Lovers</p>", unsafe_allow_html=True)
st.divider()

# 4. App Logic
try:
    data = pd.read_csv("action_movies.csv")
    
    # Sidebar Info
    st.sidebar.image("https://www.imdb.com/favicon.ico", width=50)
    st.sidebar.title("Project Stats")
    st.sidebar.write(f"📂 **Dataset:** {len(data)} Movies")
    st.sidebar.write("⚡ **Model:** TF-IDF + Cosine Similarity")
    st.sidebar.info("This project recommends movies based on semantic plot analysis.")

    # Search Bar
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        user_input = st.text_input("What's your vibe today?", placeholder="e.g. Undercover agent in a high-speed chase")
        search_btn = st.button("GET RECOMMENDATIONS", use_container_width=True)

    # Results
    if search_btn:
        if user_input:
            results = get_recommendations(user_input, data)
            
            st.write("### 🔥 Top Picks for You")
            
            for i, row in results.iterrows():
                # Displaying each movie in a custom HTML card
                st.markdown(f"""
                    <div class="movie-card">
                        <div class="movie-title">{row['Title']}</div>
                        <div class="movie-plot">{row['Storyline']}</div>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Please describe what you want to watch!")

except FileNotFoundError:
    st.error("Error: 'action_movies.csv' not found. Please run the scraper first.")