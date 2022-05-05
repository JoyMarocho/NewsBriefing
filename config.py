import os


class Config:
    NEWS_API_BASE_URL = "https://newsapi.org/v2/top-headlines/sources?apiKey={}"
    ARTICLE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    API_KEY= os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
        '''
        Development  configuration child class
        Args:
        Config: The parent configuration class with General configuration settings
        '''

DEBUG = True
    
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}