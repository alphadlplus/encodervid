import requests
import json


def IMDB(x):
    response_imdb = requests.post("http://www.omdbapi.com/?i=%s&apikey=18f7a8b7"%x)
    callback = response_imdb.content
    types = json.loads(callback)['Type'].strip("\'")
    # imdbID = json.loads(callback)['imdbID'].strip("\'")
    # title = json.loads(callback)['Title'].replace("\'","\\'")
    # year = json.loads(callback)['Year'].strip("\'")
    # result = [types,imdbID,title,year]
    return types

