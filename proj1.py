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

twitter_path = join(dirname(__file__), '../keys/twitter.env')
load_dotenv(twitter_path)

spoon_path = join(dirname(__file__), '../keys/spoonacular.env')
load_dotenv(spoon_path)

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
    msg = ''
    img = 'https://www.applesfromny.com/wp-content/uploads/2020/05/Rome_NYAS-Apples2.png'
    ing = []
    while not tweet:
        url = "https://api.spoonacular.com/recipes/random?apiKey={}".format(spoonacular_key)
        response = requests.get(url)
        json_body = response.json()
        
        if 'status' in json_body and json_body["status"] == 'failure':
            spoon = False
            break
        title = json_body["recipes"][0]["title"]
        title = title.strip('\"')
        img = json_body["recipes"][0]["image"]
        img = img.strip('\"')
        tweet =api.search(q=title,lang="en",count=100)
        json_ing = json_body["recipes"][0]["extendedIngredients"]
        ing_size = len(ing)
        for jing in json_ing:
            ing.append(jing["original"])
    print(ing)
    if not spoon:
        recipes = ['Spaghetti & Meatballs','PB&J','Scrambled Eggs','Pancakes','Ribs','Ramen','Fried Rice']
        title = recipes[random.randint(0,6)]
        tweet =api.search(q=title,lang="en",count=100)
        msg = "Spoonacular has reached the max number of requests. Picking a recipe from memory."
    size = len(tweet)
    print(size)
    num = random.randint(0,size-1)
    text = tweet[num].text
    screen_name = tweet[num].user.screen_name
    date = tweet[num].created_at
    
    return flask.render_template(
        "index.html",
        msg=msg,
        title = title,
        text = text,
        screen_name = screen_name,
        date = date,
        img=img,
        ing=ing
        )
    
        
        
app.run(
    port = int(os.getenv("PORT", 8080)),   
    host = os.getenv("IP", "0.0.0.0")
)