from utils import scraper_v1
from utils import sentiment
from utils.llm import GroqChatClient

groq_client = GroqChatClient()

def main(company_name):
    result = {}
    result["company"] = company_name

    articles = scraper_v1.main(company_name)
    article_data = []

    for article in articles:

        each_article_data = {}

        article_sentiment = sentiment.analyze_sentiment(article)

        summary = groq_client.chat(f"Give me a super short summary of this web article: {article}")
        
        title = groq_client.chat(f"Give me a super short title of this summary, your output format must be a single title: {summary}")

        topics = groq_client.chat(f'Generate a list consisting of 3-4 relevant topics that my web article deals with, your output must be in this format ["topic1", "topic2", "topic3"]:. Article: {article} ')
        
        each_article_data["title"] = title
        each_article_data["summary"] = summary
        each_article_data["sentiment"] = article_sentiment
        each_article_data["topics"] = topics
        article_data.append(each_article_data)
        # break
    result["articles"] = article_data
    return result
temp = {'company': 'microsoft', 'articles': [{'title': 'Microsoft-OpenAI Deal Clears UK Competition Scrutiny \n', 'summary': "The UK's competition regulator has cancelled its investigation into Microsoft's partnership with OpenAI, due to insufficient evidence of harm to competition in the AI field.  \n", 'sentiment': 'Positive', 'topics': '["Competition Law", "Artificial Intelligence", "Microsoft", "OpenAI"] \n'}, {'title': 'Skype to Shut Down Apps \n', 'summary': 'Skype will shut down its desktop and mobile apps in May 2023.  \n', 'sentiment': 'Positive', 'topics': '["Webinar Software", "Remote Communication", "Microsoft Products"] \n'}, {'title': 'Quantum Leap: Microsoft Predicts Near-Term Quantum Advancements \n', 'summary': 'Microsoft predicts powerful quantum computers will be available within years, not decades. They believe advancements in their new chip architecture will allow for faster development and deployment of these next-generation computers.  \n', 'sentiment': 'Positive', 'topics': '["Quantum Computing", "Microsoft Research", "Technological Advancements", "Artificial Intelligence"] \n\n\nLet me know if you\'d like me to elaborate on any of these topics! \n'}, {'title': 'Manchester: Tech Town  \n', 'summary': 'A new exhibition in Manchester, England, celebrates the city\'s origins as a center for technological innovation, nicknamed "Tech Town".  \n', 'sentiment': 'Positive', 'topics': '["Technology History", "Urban Development", "Exhibition Reviews", "Community Identity"] \n'}, {'title': 'Amazon Enters Quantum Race with "Cat-Qubit" Chip  \n', 'summary': 'Amazon has unveiled a new chip powered by "cat-qubit" technology, a type of qubit that\'s more stable than traditional ones. This move puts Amazon officially in the race to build powerful quantum computers.  \n', 'sentiment': 'Positive', 'topics': '["Quantum Computing", "Amazon", "Quantum Hardware", "Cat Qubits"] \n'}, {'title': 'AI Enhances Learning at British School \n', 'summary': 'The BBC article discusses how a British school is utilizing artificial intelligence (AI) to enhance the learning experience for students.  \n\n', 'sentiment': 'Positive', 'topics': '["Artificial Intelligence in Education", "AI Applications in Schools", "Benefits of AI in Learning", "Ethical Considerations of AI in Education"] \n'}, {'title': 'Quantum Computing: Disrupting Business Sectors \n', 'summary': 'The article explores the potential impact of quantum computing on various business sectors.  It highlights how this emerging technology could revolutionize fields like drug discovery, materials science, and finance by solving complex problems beyond the capabilities of classical computers.  \n', 'sentiment': 'Positive', 'topics': '["quantum computing", "business applications", "future of technology", "innovation"] \n'}, {'title': 'Nvidia AI Chip Sales Soar Despite Slowdown Fears \n', 'summary': 'Despite concerns about a slowdown in demand for AI chips, Nvidia, a leading chipmaker, reports strong sales of its artificial intelligence (AI) processing units.  \n', 'sentiment': 'Positive', 'topics': '["Nvidia\'s Financial Performance", "AI Chip Market", "DeepSearch\'s Impact on AI Industry", "Technological Advancements"] \n'}, {'title': 'Women Journalists Expose Bribery \n', 'summary': 'This BBC article page highlights an Audio segment from "The Conversation" podcast focusing on women journalists investigating bribery and corruption.  \n', 'sentiment': 'Positive', 'topics': '["investigative journalism", "bribery and corruption", "women in journalism", "gender bias"] \n'}]}

temp2 = {'sentiment_distribution': {'Positive': 9, 'Negative': 0, 'Neutral': 0}, 'coverage_differences': [{'comparison': "While the first article focuses on Microsoft's successful navigation of UK competition rules for its OpenAI partnership, the rest explore diverse tech trends  in areas like quantum computing, AI, and journalism.  \n\n", 'impact': "The first article focuses on regulatory approval for Microsoft's AI partnership while the others explore diverse tech advancements and trends. \n\n"}], 'topic_overlap': {'common_topics': '["Competition Law", "Artificial Intelligence", "Microsoft", "OpenAI", "Webinar Software", "Remote Communication", "Quantum Computing", "Technological Advancements", "Technology History", "Urban Development", "Exhibition Reviews", "Community Identity", "Quantum Hardware", "Cat Qubits", "AI Applications", "Business Applications", "AI Chip Market", "DeepSearch", "Nvidia\'s Financial Performance",  "Ethical Considerations", "Innovation", "investigative journalism", "bribery and corruption", "women in journalism", "gender bias"] \n\n\n', 'unique_topics_of_article_1': '["Competition Law", "Artificial Intelligence", "Microsoft", "OpenAI"]', 'unique_topics_of_article_2': '["Webinar Software", "Remote Communication", "Microsoft Products"]', 'unique_topics_of_article_3': '["Quantum Computing", "Microsoft Research", "Technological Advancements", "Artificial Intelligence"] \n\n\nLet me know if you\'d like me to elaborate on any of these topics!', 'unique_topics_of_article_4': '["Technology History", "Urban Development", "Exhibition Reviews", "Community Identity"]', 'unique_topics_of_article_5': '["Quantum Computing", "Amazon", "Quantum Hardware", "Cat Qubits"]', 'unique_topics_of_article_6': '["Artificial Intelligence in Education", "AI Applications in Schools", "Benefits of AI in Learning", "Ethical Considerations of AI in Education"]', 'unique_topics_of_article_7': '["quantum computing", "business applications", "future of technology", "innovation"]', 'unique_topics_of_article_8': '["Nvidia\'s Financial Performance", "AI Chip Market", "DeepSearch\'s Impact on AI Industry", "Technological Advancements"]', 'unique_topics_of_article_9': '["investigative journalism", "bribery and corruption", "women in journalism", "gender bias"]'}, 'final_sentiment': 'The articles exarket", "DeepSearch\'s Impact on AI Industry", "Technological Advancements"]'}

def comparative_analysis(company_name):
    result = temp#main(company_name)
    return {**temp, **temp2}
    final_result = {}
    sentiments = []
    from collections import Counter  
 


    for article in result['articles']:
        sentiments.append(article['sentiment'])
    freq = Counter(sentiments) 
    stmt = ["Positive", "Negative", "Neutral"] 
    final_result['sentiment_distribution'] = {x: freq[x] for x in stmt} 
    
    # COMPARISON
    # Extract titles
    titles = [article['title'].strip() for article in result['articles']]
    coverage_differences = []
    for i in range(len(titles)):
        current_title = titles[i]
        rest_of_titles = titles[:i] + titles[i+1:]  # Excludes the current element

        comparison = groq_client.chat(f'Generate a comparison between the first article and the rest of the article in one sentence. \
        1. Article : {current_title}, \
        2. other articles: {rest_of_titles}. \
        Keep you response concise')
        impact = groq_client.chat(f'Generate a comparison between the first article and the rest of the article in one sentence. \
        1. Article : {current_title}, \
        2. other articles: {rest_of_titles}. \
        Keep you response concise')
        coverage_differences.append({'comparison':comparison, 'impact':impact})
        break
    final_result['coverage_differences'] = coverage_differences
    # topics
    topics = [article['topics'].strip() for article in result['articles']]
    topic_result = {}
    for i, topic in enumerate(topics):
        topic_result[f'unique_topics_of_article_{i+1}'] = topic
    
    common_topic = groq_client.chat(f'Give me all common topics from all the individual topics in a single list \
    topics : {topics}, Keep you response concise and just the list of common topics\
    example strict output should be as the following: "["technology", "LLM" , "engineering"]"')
    final_result['topic_overlap'] = {"common_topics":common_topic,  **topic_result}

    final_sentiment = groq_client.chat(f'Generate a final sentiment analysis of all the articles in one sentence. \
    Articles : {titles}, \
    Keep you response concise')
    final_result['final_sentiment'] = final_sentiment

    return { **result, **final_result}
# print(comparative_analysis("microsoft"))