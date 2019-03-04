import os

class Config:

    BLOG_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json' 

    BLOG_API_KEY = os.environ.get('BLOG_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexianne:wecode@localhost/blogpost'
   
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    # email configurations
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREF = 'Webapp'
    SENDER_EMAIL  = 'imalexianne@gmail.com'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexianne:wecode@localhost/blogpost'
    DEBUG = True


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexianne:wecode@localhost/blogpost'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}