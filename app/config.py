class Config:
    NEWS_API_URL = 'https://newsapi.org/v2/everything?q=Apple&from=2022-04-29&sortBy={}&apiKey={}'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True