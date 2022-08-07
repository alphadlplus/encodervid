
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    APP_ID = os.environ.get('APP_ID', None)
    API_HASH = os.environ.get('API_HASH', None)
    API_URL = os.environ.get('API_URL', None)
    CHANNEL_MOVIE = -1001449081541
    CHANNEL_SERIES = -1001477968568
    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','237379411').split(',')]

    DOWNLOAD_DIR = 'downloads'
