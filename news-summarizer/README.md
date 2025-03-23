News Summarization & Sentiment Analysis

📌 Overview

This project provides news summarization, sentiment analysis, and text-to-speech (TTS) conversion for company-related news articles. Users can enter a company name and receive summarized news, sentiment insights, and an option to generate Hindi speech output.

🚀 Features

News Summarization: Fetches and summarizes news articles related to a given company.

Sentiment Analysis: Analyzes the sentiment of the news articles (Positive, Negative, or Neutral).

Comparative Analysis: Compares sentiment trends across multiple articles.

Text-to-Speech (TTS): Converts news summaries into Hindi audio.

🛠️ Technologies Used

Backend: FastAPI

Frontend: Streamlit

Web Scraping: BeautifulSoup, Requests

NLP: NLTK, Sumy

Text-to-Speech: gTTS (Google Text-to-Speech)

Project Structure

news-summarizer/
│── api.py               # FastAPI backend
│── frontend.py          # Streamlit frontend
│── utils/
│   ├── scraper.py      # Scrapes news articles
│   ├── sentiment.py    # Performs sentiment analysis
│   ├── summarizer.py   # Summarizes news text
│   ├── texttospeech.py # Generates TTS output
│── requirements.txt     # Python dependencies
│── README.md            # Documentation


🖥️ Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/your-username/news-summarizer.git
cd news-summarizer

2️⃣ Create a virtual environment

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Run the FastAPI backend

uvicorn api:app --reload

5️⃣ Run the Streamlit frontend

streamlit run frontend.py

🎯 Future Enhancements

🔹 Improve sentiment analysis using a more advanced ML model.

🔹 Support more languages for text-to-speech.

🔹 Add visual charts for sentiment trends.

