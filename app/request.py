import urllib.request,json
from .models import Quote
# from app import app
# Getting api key
# api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global base_url
#     base_url = app.config['QUOTE_API_BASE_URL']

def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    base_url = 'http://quotes.stormconsultancy.co.uk/random.json' 
    print(base_url)

    with urllib.request.urlopen(base_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quote_object = None

        if get_quotes_response:
            id=get_quotes_response.get('id')
            author=get_quotes_response.get('author')
            quote=get_quotes_response.get('quote')
            quote_object = Quote(id,author,quote)

    return quote_object