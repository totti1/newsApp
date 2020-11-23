import os
class Config:
    NEWS_API_LINK = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    pass

class DevConfig(Config):
    # NEWS_API_LINK = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'
    DEBUG = True