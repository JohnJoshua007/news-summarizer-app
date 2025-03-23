# from fastapi import APIRouter
from utils.scraper import get_news_articles
from utils.sentiment import analyze_sentiment
from utils.summarizer import summarize_text
# from utils.texttospeech import generate_tts
from main import main, comparative_analysis
# router = APIRouter()

# @router.get("/news/{company}")
# def fetch_news(company: str):
#     articles = get_news_articles(company)
#     return {"articles": articles}

# @router.get("/sentiment/{company}")
# def fetch_sentiment(company: str):
#     articles = get_news_articles(company)
#     sentiment_results = [analyze_sentiment(a["summary"]) for a in articles]
#     return {"sentiments": sentiment_results}

# @router.get("/summary/{company}")
# def fetch_summary(company: str):
#     articles = get_news_articles(company)
#     summaries = [summarize_text(a["summary"]) for a in articles]
#     return {"summaries": summaries}

# @router.get("/tts/{company}")
# def fetch_tts(company: str):
#     articles = get_news_articles(company)
#     text = " ".join([a["summary"] for a in articles])
#     audio_file = generate_tts(text)
#     return {"tts_audio": audio_file}


# from fastapi import FastAPI

# app = FastAPI()  # ✅ Make sure this exists

# @app.get("/")
# def read_root():
#     return {"message": "API is working!"}
# # print("Fetched articles:", articles)

from fastapi import FastAPI, Query
from gtts import gTTS

app = FastAPI()

@app.get("/get_news")
def get_news(company: str):

    result = comparative_analysis(company)
    return result


# @app.get("/get_tts")
# def get_tts(company: str):
#     return {"tts_audio": "audio_file.mp3"}

from utils import texttospeech
import asyncio
import json
@app.get("/get_tts")
def get_tts(text: str = Query(..., description="Text to convert to speech")):
    if not text.strip():
        return {"error": "No text to speak"}  
    text = json.loads(text)
    articles = text["articles"]
    final_text = ""
    for i, each_article in enumerate(articles):
        final_text = final_text + " " + f"The summary of article {i} is " +  each_article['summary']
    file_path = "output.mp3"
    asyncio.run(texttospeech.text_to_hindi_speech(final_text, output_file=file_path))


    return {"tts_audio": file_path}

 