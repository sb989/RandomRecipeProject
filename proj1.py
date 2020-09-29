import tweepy
import os
import datetime
import flask
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import json
import random
from helper_functions import load_random_recipe,save_recipe,search_results,load_recipe

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

carrot = '/static/carrot.png'
peopleimg = '/static/people.png'
clockimg = '/static/clock.png'
img = 'https://spoonacular.com/cdn/ingredients_500x500/apple.jpg'
ing = []
servings = 0
time = 0 

@app.route('/load_online/<id_num>')
def recipe_online(id_num):
    tweet = []
    original_site = ''
    screen_name = ''
    date = ''
    msg = ''
    title=''
    text =''
    url = 'https://api.spoonacular.com/recipes/{}/information?apiKey={}'.format(id_num,spoonacular_key)
    response = requests.get(url)
    json_body = response.json()
    print(json_body)
    if 'status' in json_body and json_body["status"] == 'failure':
        msg = "Spoonacular has reached the max number of requests. Cannot load the specified recipe."
        return flask.render_template(
        'error.html',
        msg=msg,
        carrot=carrot
        )
    
    img = json_body["image"]
    img = img.strip('\"')
    title = json_body["title"]
    title = title.strip('\"')
    
    original_site = json_body["sourceUrl"]
    tweet =api.search(q=title,lang="en",count=100)
    json_ing = json_body["extendedIngredients"]
    ing_size = len(ing)
    time = json_body["readyInMinutes"]
    servings = json_body["servings"]
    for jing in json_ing:
        ing.append(jing["original"])
    
    size = len(tweet)
    if(size > 0):
        num = random.randint(0,size-1)
        text = tweet[num].text
        screen_name = tweet[num].user.screen_name
        date = tweet[num].created_at
    else:
        text = 'No tweets found'
    
    return flask.render_template(
        'index.html',
         msg = msg,
        title = title,
        text = text,
        screen_name = screen_name,
        date = date,
        img = img,
        ing = ing,
        servings = servings,
        time = time,
        people = peopleimg,
        clock = clockimg,
        original_site = original_site,
        carrot=carrot
        )

@app.route('/load_local/<index>')
def recipe_local(index):
    
    tweet = []
    original_site = ''
    screen_name = ''
    date = ''
    msg = ''
    
    json_body = load_recipe(int(index))
    img = json_body["image"]
    img = img.strip('\"')
    title = json_body["title"]
    title = title.strip('\"')
    
    original_site = json_body["sourceUrl"]
    tweet =api.search(q=title,lang="en",count=100)
    json_ing = json_body["extendedIngredients"]
    ing_size = len(ing)
    time = json_body["readyInMinutes"]
    servings = json_body["servings"]
    for jing in json_ing:
        ing.append(jing["original"])
    
    size = len(tweet)
    if(size > 0):
        num = random.randint(0,size-1)
        text = tweet[num].text
        screen_name = tweet[num].user.screen_name
        date = tweet[num].created_at
    else:
        text = 'No tweets found'
    return flask.render_template(
        'index.html',
        msg = msg,
        title = title,
        text = text,
        screen_name = screen_name,
        date = date,
        img = img,
        ing = ing,
        servings = servings,
        time = time,
        people = peopleimg,
        clock = clockimg,
        original_site = original_site,
        carrot=carrot
        )

@app.route('/results.html',methods=['POST','GET'])
def results():
    search = flask.request.form['recipe']
    print(search)
    url = "https://api.spoonacular.com/recipes/complexSearch?query={}&apiKey={}".format(search,spoonacular_key)
    response = requests.get(url)
    json_body = response.json()
    msg = ''
    if 'status' in json_body and json_body["status"] == 'failure':
        msg = "Spoonacular has reached the max number of requests. Picking a recipe from memory."
        json_body = search_results(search)
        #print(results["results"])
    
    
    return flask.render_template('results.html',
    carrot=carrot,
    msg=msg,
    results=json_body["results"]
    )

@app.route('/')
def index():
    original_site = ''
    screen_name = '@'
    date = ''
    tweet = []
    msg = ''
    while not tweet:
        url = "https://api.spoonacular.com/recipes/random?apiKey={}".format(spoonacular_key)
        response = requests.get(url)
        json_body = response.json()
        
        if 'status' in json_body and json_body["status"] == 'failure':
            json_body = load_random_recipe()
            msg = "Spoonacular has reached the max number of requests. Picking a recipe from memory."
        else:
            json_body = json_body["recipes"][0]
            save_recipe(json_body)
            
        title = json_body["title"]
        title = title.strip('\"')
        if "image" not in json_body:
            continue
        img = json_body["image"]
        img = img.strip('\"')
    
        original_site = json_body["sourceUrl"]
        tweet =api.search(q=title,lang="en",count=100)
        json_ing = json_body["extendedIngredients"]
        ing_size = len(ing)
        time = json_body["readyInMinutes"]
        servings = json_body["servings"]
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
        msg = msg,
        title = title,
        text = text,
        screen_name = screen_name,
        date = date,
        img = img,
        ing = ing,
        servings = servings,
        time = time,
        people = peopleimg,
        clock = clockimg,
        original_site = original_site,
        carrot=carrot
        )
    
        
        
app.run(
    port = int(os.getenv("PORT", 8080)),   
    host = os.getenv("IP", "0.0.0.0"),
    debug=True
)



    
