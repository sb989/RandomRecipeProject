import tweepy
import os
import datetime
import flask
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import json
import random

app = flask.Flask(__name__)

dotenv_path = join(dirname(__file__), '../twitter.env')
load_dotenv(dotenv_path)

dotenv_path = join(dirname(__file__), '../spoonacular.env')
load_dotenv(dotenv_path)

spoonacular_key = os.environ['SPOONACULAR_KEY']

consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_S_KEY")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_S")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)






@app.route('/')
def index():
    tweet = []
    spoon = True
    while not tweet:
        url = "https://api.spoonacular.com/recipes/random?apiKey={}".format(spoonacular_key)
        response = requests.get(url)
        json_body = response.json()
        
        if json_body["status"] == 'failure':
            spoon = False
            break
        title = json_body["recipes"][0]["title"]
        title = title.strip('\"')
        print(title)
        tweet =api.search(q=title,lang="en",count=100)
    if spoon:
        size = len(tweet)
        print(size)
        num = random.randint(0,size-1)
        text = tweet[num].text
        screen_name = tweet[num].user.screen_name
        date = tweet[num].created_at
        return flask.render_template(
            "index.html",
            title = title,
            text = text,
            screen_name = screen_name,
            date = date
            )
    else:
        msg = "Sorry. We've reached the max number of recipes for today. Please try again tomorrow."
        return flask.render_template(
            "index.html",
            msg=msg
            )
        
app.run(
    port = int(os.getenv("PORT", 8080)),   
    host = os.getenv("IP", "0.0.0.0")
)