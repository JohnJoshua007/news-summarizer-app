from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

# def analyze_sentiment(text):
#     sia = SentimentIntensityAnalyzer()
#     score = sia.polarity_scores(text)
#     if score["compound"] >= 0.05:
#         return "Positive"
#     elif score["compound"] <= -0.05:
#         return "Negative"
#     else:
#         return "Neutral"

def analyze_sentiment(text):
    if not text.strip():
        return {"Sentiment": "Neutral", "Score": 0.5}  # Default neutral for empty text

    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)
    
    sentiment = "Neutral"
    if score["compound"] >= 0.05:
        sentiment = "Positive"
    elif score["compound"] <= -0.05:
        sentiment = "Negative"

    normalized_score = (score["compound"] + 1) / 2

    return sentiment#{"Sentiment": sentiment, "Score": round(normalized_score, 3)}
