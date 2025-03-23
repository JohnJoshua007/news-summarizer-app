# import streamlit as st
# import requests

# st.title("📢 News Summarization & Sentiment Analysis")

# company = st.text_input("Enter Company Name")

# if st.button("Get News Summary"):
#     response = requests.get(f"http://127.0.0.1:8000/get_news?company={company}")
#     if response.status_code == 200:
#         articles = response.json().get("Articles", [])
#         for article in articles:
#             st.subheader(article["Title"])  # Fix key case
#             st.write(article["Summary"])  # Fix key case
#             st.write(article["link"])
#     else:
#         st.error("Failed to fetch news.")

# if st.button("Get Sentiment Analysis"):
#     response = requests.get(f"http://127.0.0.1:8000/get_sentiment?company={company}")
#     if response.status_code == 200:
#         sentiment = response.json().get("Sentiment", "Unknown")
#         st.write(f"Sentiment Analysis: {sentiment}")
#     else:
#         st.error("Sentiment analysis failed.")

# if st.button("Generate Hindi Speech"):
#     response = requests.get(f"http://127.0.0.1:8000/get_tts?company={company}")
#     if response.status_code == 200:
#         audio_file = response.json().get("tts_audio", "")
#         if audio_file:
#             st.audio(audio_file, format="audio/mp3")
#         else:
#             st.error("Audio file not found.")
#     else:
#         st.error("Failed to generate speech.")

# # Debugging: Test API request separately
# # response = requests.get(f"http://127.0.0.1:8000/get_news?company=Oracle")
# # print("API Response:", response.json())  # Debugging output



# import streamlit as st
# import requests
# import time

# # Set page configuration
# st.set_page_config(page_title="News & Sentiment Analysis", page_icon="📢", layout="wide")

# # Custom CSS for background color & better visuals
# st.markdown("""
#     <style>
#         /* Background Gradient */
#         body {
#             background: linear-gradient(to right, #f3f4f6, #dde1e7);
#         }
        
#         /* Styling for headings and text */
#         .big-font { font-size:20px !important; font-weight: bold; }
#         .sub-font { font-size:18px !important; color: #666; }
        
#         /* Button styling */
#         .stButton>button {
#             width: 100%;
#             border-radius: 10px;
#             background: #4CAF50;
#             color: white;
#             font-size: 18px;
#             padding: 10px;
#         }
        
#         /* Card styling */
# .st-card {
#     background: white;
#     padding: 15px;
#     border-radius: 10px;
#     box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
#     margin-bottom: 20px; /* Adds spacing between cards */
# }

#     </style>
# """, unsafe_allow_html=True)

# # Title with custom color
# st.markdown("<h1 style='text-align: center; color: #2E3A87;'>📢 News Summarization & Sentiment Analysis</h1>", unsafe_allow_html=True)
# st.markdown("<p class='sub-font' style='text-align: center;'>🔍 Get summarized news and sentiment insights for your favorite companies! It's absolutely Free!!!</p>", unsafe_allow_html=True)

# # Input field
# company = st.text_input("✍️ **Enter Company Name**")

# # Use columns for better layout
# col1, col2, col3 = st.columns(3)
# with col1:
#     if st.button("📄 Get News Summary"):
#         with st.spinner("Fetching latest news..."):
#             time.sleep(1)  # Simulate loading
#             response = requests.get(f"http://127.0.0.1:8000/get_news?company={company}")
#             if response.status_code == 200:
#                 data = response.json()
#                 articles = data.get("articles", [])
#                 if articles:
#                     st.subheader(f"Latest News for {data.get('company', 'Unknown')}")
#                     for article in articles:
#                         sentiment_color = "green" if article["sentiment"].lower() == "positive" else "red"
#                         st.markdown(
#                             f"""
#                             <div style='border:1px solid #ddd; padding:10px; border-radius:10px; margin-bottom:10px;'>
#                                 <h3 style='color:{sentiment_color};'>📰 {article.get('title', 'No Title')}</h3>
#                                 <p>{article.get('summary', 'No Summary Available')}</p>
#                                 <p><b>Sentiment:</b> {article.get('sentiment', 'Unknown')}</p>
#                                 <p><b>Topics:</b> {article.get('topics', []) if article.get('topics') else 'None'}</p>
#                             </div>
#                             """,
#                             unsafe_allow_html=True
#                         )
#                 else:
#                     st.warning("No news articles found.")
#             else:
#                 st.error("Failed to fetch news.")

# with col2:
#     if st.button("📊 Get Sentiment Analysis"):
#         with st.spinner("Analyzing sentiment..."):
#             time.sleep(1)  # Simulate processing
#             response = requests.get(f"http://127.0.0.1:8000/get_sentiment?company={company}")
#             if response.status_code == 200:
#                 sentiment = response.json().get("Sentiment", "Unknown")
#                 score = response.json().get("Score", 0)  # Assuming a score between 0-1
#                 st.markdown(f"<div class='st-card'><h3>🧐 Sentiment Analysis</h3><p>**{sentiment}**</p></div>", unsafe_allow_html=True)
#                 st.progress(score)  # Show sentiment score visually
#             else:
#                 st.error("Sentiment analysis failed.")

# with col3:
#     if st.button("🗣️ Generate Hindi Speech"):
#         with st.spinner("Generating speech..."):
#             time.sleep(1)  # Simulate processing
#             response = requests.get(f"http://127.0.0.1:8000/get_tts?company={company}")
#             if response.status_code == 200:
#                 audio_file = response.json().get("tts_audio", "")
#                 if audio_file:
#                     st.audio(audio_file, format="audio/mp3")
#                 else:
#                     st.error("Audio file not found.")
#             else:
#                 st.error("Failed to generate speech.")

# # Footer
# st.markdown("<hr>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center;'>🎯 Built with ❤️ using <strong>Streamlit</strong></p>", unsafe_allow_html=True)


import streamlit as st
import requests
import time

# Set page configuration
st.set_page_config(page_title="News & Sentiment Analysis", page_icon="📢", layout="wide")

# Custom CSS for background color & better visuals
st.markdown("""
    <style>
        /* Background Gradient */
        body {
            background: linear-gradient(to right, #1e1e2e, #25293d);
            color: white;
        }
        
        /* Styling for headings and text */
        .big-font { font-size:20px !important; font-weight: bold; }
        .sub-font { font-size:18px !important; color: #bbb; }
        
        /* Button styling */
        .stButton>button {
            width: 90%;
            border-radius: 8px;
            background: #4CAF50;
            color: white;
            font-size: 14px;
            padding: 8px;
        }

        /* Card styling */
        .st-card {
            background: #2E3A87;
            color: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px; /* Adds spacing between cards */
        }
    </style>
""", unsafe_allow_html=True)

# Title with custom color
st.markdown("<h1 style='text-align: center; color: #2E3A87;'>📢 News Summarization & Sentiment Analysis</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-font' style='text-align: center;'>🔍 Get summarized news and sentiment insights for your favorite companies! It's absolutely Free!!!</p>", unsafe_allow_html=True)

# Input field
company = st.text_input("✍️ **Enter Company Name**")

# Use columns for better layout (4 buttons now)
col1, col2, col3= st.columns(3)

with col1:
    if st.button("📄 Get News Summary"):
        with st.spinner("Fetching latest news..."):
            # time.sleep(1)  # Simulate loading
            response = requests.get(f"http://127.0.0.1:8000/get_news?company={company}")
            if response.status_code == 200:
                data = response.json()
                if "entire_result" not in st.session_state:
                    st.session_state["entire_result"] = data
                articles = data.get("articles", [])
                if articles:
                    st.subheader(f"Latest News for {data.get('company', 'Unknown')}")
                    for article in articles:
                        sentiment_color = "green" if article["sentiment"].lower() == "positive" else "red"
                        st.markdown(
                            f"""
                            <div style='border:1px solid #ddd; padding:10px; border-radius:10px; margin-bottom:10px;'>
                                <h3 style='color:{sentiment_color};'>📰 {article.get('title', 'No Title')}</h3>
                                <p>{article.get('summary', 'No Summary Available')}</p>
                                <p><b>Sentiment:</b> {article.get('sentiment', 'Unknown')}</p>
                                <p><b>Topics:</b> {article.get('topics', []) if article.get('topics') else 'None'}</p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                else:
                    st.warning("No news articles found.")
            else:
                st.error("Failed to fetch news.")

# with col2:
#     if st.button("🎭 Get Sentiment Analysis"):
#         with st.spinner("Analyzing sentiment..."):
#             # time.sleep(1)  # Simulate processing
#             response = st.session_state["entire_result"]

#             if response:
#                 sentiment = response.get("Sentiment", "Unknown")
#                 score = response.json().get("Score", 0)  # Assuming a score between 0-1
#                 st.markdown(f"<div class='st-card'><h3>🧐 Sentiment Analysis</h3><p>**{sentiment}**</p></div>", unsafe_allow_html=True)
#                 st.progress(score)  # Show sentiment score visually
#             else:
#                 st.error("Sentiment analysis failed.")
import pandas as pd
with col2:
    if st.button("📊 Get Comparative Analysis"):
        with st.spinner("Comparing companies..."):
            response = st.session_state["entire_result"]
            
            # Title
            st.title("📊 Article Analysis Dashboard")

            # Sentiment Distribution Chart
            st.subheader("📈 Sentiment Distribution")
            sentiment_df = pd.DataFrame(
                list(response["sentiment_distribution"].items()), 
                columns=["Sentiment", "Count"]
            )
            st.bar_chart(sentiment_df.set_index("Sentiment"))

            # Coverage Differences
            st.subheader("📌 Coverage Differences")
            st.markdown(f"**Comparison:** {response['coverage_differences'][0]['comparison']}")
            st.markdown(f"**Impact:** {response['coverage_differences'][0]['impact']}")

            # Topic Overlap
            st.subheader("🗂 Topic Analysis")
            st.markdown(f"**Common Topics:** {response['topic_overlap']['common_topics']}")

            # Extracting Unique Topics
            st.markdown("### 🔍 Unique Topics in Articles")

            for key, topics in response["topic_overlap"].items():

                if key.startswith("unique_topics_of_article_"):

                    article_num = key.split("_")[-1]  # Extracting article 
                    st.write(f"**Article {article_num}:** {topics}")
                    st.markdown(f"**Article {article_num}:** {topics}")

            # Final Sentiment Summary
            st.subheader("📝 Final Sentiment Summary")
            st.write(response["final_sentiment"])
import json
with col3:
    if st.button("🗣️ Generate Hindi Speech"):
        with st.spinner("Generating speech..."):
            if company.strip():
                response = requests.get(f"http://127.0.0.1:8000/get_tts?text={json.dumps(st.session_state["entire_result"])}")
                if response.status_code == 200:
                    audio_file = response.json().get("tts_audio", "")
                    if audio_file:
                            st.audio(audio_file, format="audio/mp3")
                    else:
                        st.error("Audio file not found.")
                else:
                    st.error("Failed to generate speech.")
            else:
                st.warning("⚠️ Please enter a company name before generating speech.")


# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>🎯 Built with ❤️ using <strong>Streamlit</strong></p>", unsafe_allow_html=True)
