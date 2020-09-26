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

spoonacular_key = os.getenv('SPOONACULAR_KEY')

consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_S_KEY")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_S")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def save_recipe(recipe):
    file = open('recipes.json','r')
    recipes = json.load(file)
    if recipes["nextEntry"]==200:
        recipes["recipes"].pop(0)
    else:
        recipes["nextEntry"]+=1
    recipes["recipes"].append(recipe)
    file.close()
    file = open('recipes.json','w')
    json.dump(recipes,file,indent=4)
    file.close()

def load_recipe():
    file = open('recipes.json','r')
    recipes = json.load(file)
    size = recipes["nextEntry"]
    entry = random.randint(0,size-1)
    recipe = recipes["recipes"][entry]
    return recipe
    
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
        json_body = json_body["recipes"][0]
        if 'status' in json_body and json_body["status"] == 'failure':
            json_body = load_recipe()
            msg = "Spoonacular has reached the max number of requests. Picking a recipe from memory."
        else:
            save_recipe(json_body)
        title = json_body["title"]
        title = title.strip('\"')
        if "image" in json_body:
            img = json_body["image"]
            img = img.strip('\"')
        tweet =api.search(q=title,lang="en",count=100)
        json_ing = json_body["extendedIngredients"]
        ing_size = len(ing)
        
        for jing in json_ing:
            ing.append(jing["original"])
    
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


#def load_recipe():
    
