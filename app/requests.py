from app import app
import urllib.request,json
from .models import news

# News = news.News

api_key = app.config['NEWS_API_KEY']

base_url = app.config['NEWS_API_URL']

def get_news(popularity):
    get_news_url = base_url.format(popularity, api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        news_data = url.read()
        news_data_dict = json.loads(news_data)
        
        news_results = None
        
        if news_data_dict['articles']:
            news_results_list = news_data_dict['articles']
            news_results = process_news(news_results_list)
            
        return news_results
    
def process_news(news_list, ):
    news_results = []
    for news_item in news_list:
        # news_items_data = image, description, time
        # image = news_item.get('image')
        description = news_item.get('description')
        # time = news_item.get('time')
        
        news_results.append(description)
        
    return news_results
        
        # if news__exist:
        #     news_object = News(image, description, time)
        #     news_results.append(news_object)
    