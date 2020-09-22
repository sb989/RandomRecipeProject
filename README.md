Follow these steps to get this repository running:
1. Sign up for a twitter developer account if you dont already have one at https://developer.twitter.com
2. Navigate to https://developer.twitter.com/en/portal/projects-and-apps and click Create App
3. Click on the key symbol to retrieve your api keys and access tokens
4. Sign up for a spoonacular api account by going to https://spoonacular.com/food-api/console#Dashboard
5. After logging in head to https://spoonacular.com/food-api/console#Profile to obtain your spoonacular api key
6. Clone this repo by executing git clone https://github.com/NJIT-CS490/project1-sb989.git
7. Install tweepy by performing one of the following commands on your terminal:
    sudo pip install tweepy
    sudo pip3 install tweepy
    pip install tweepy
    pip3 install tweepy
8. Install flask and python-dotenv by using one of the commands above, and replacing tweepy with the name of the program (e.g. pip install flask)
9. Create a file called twitter.env and place your twitter keys and tokens in there. It should look like this:
    API_KEY='xxxxx'
    API_S_KEY='xxxxx'
    ACCESS_TOKEN='xxxxx'
    ACCESS_TOKEN_S='xxxxx'
10. Create a file called spoonacular.env and place your spoonacular api key in there. It should look like this:
    SPOONACULAR_KEY='xxxxx'
11. twitter.env and spoonacular.env can be placed anywhere as long as the paths in proj1.py are correct.
    For example, if twitter.env is placed in the same folder as this repo then in proj1.py  
    twitter_path = join(dirname(__file__), 'twitter.env'). The same applies to spoon_path in proj1.py
12. If the .env files are placed anywhere in the same folder as this repo, be sure to create a .gitignore and include twitter.env and spoonacular.env in it
13. Run `python proj1.py`
14. If on cloud9 clicking Preview, then Preview Running Application, should open the site
