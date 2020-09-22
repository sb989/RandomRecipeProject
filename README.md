## Follow these steps to get this repository running:
1. Sign up for a twitter developer account if you dont already have one at https://developer.twitter.com
2. Navigate to https://developer.twitter.com/en/portal/projects-and-apps and click Create App
3. Click on the key symbol to retrieve your api keys and access tokens
4. Sign up for a spoonacular api account by going to https://spoonacular.com/food-api/console#Dashboard
5. After logging in head to https://spoonacular.com/food-api/console#Profile to obtain your spoonacular api key
6. Clone this repo by executing git clone `https://github.com/NJIT-CS490/project1-sb989.git`
7. Install tweepy by performing one of the following commands on your terminal:
    * sudo pip install tweepy
    * sudo pip3 install tweepy
    * pip install tweepy
    * pip3 install tweepy
8. Install flask and python-dotenv by using one of the commands above, and replacing tweepy with the name of the program (e.g. pip install flask)
9. Create a file called twitter.env and place your twitter keys and tokens in there. It should look like this:
    * API_KEY='xxxxx'
    * API_S_KEY='xxxxx'
    * ACCESS_TOKEN='xxxxx'
    * ACCESS_TOKEN_S='xxxxx'
10. Create a file called spoonacular.env and place your spoonacular api key in there. It should look like this:
    * SPOONACULAR_KEY='xxxxx'
11. twitter.env and spoonacular.env can be placed anywhere as long as the paths in proj1.py are correct.
    * For example, if twitter.env is placed in the same folder as this repo then in proj1.py : 
        * twitter_path = join(dirname(__file__), 'twitter.env') 
    * The same applies to spoon_path in proj1.py
12. If the .env files are placed anywhere in the same folder as this repo, be sure to create a .gitignore and include twitter.env and spoonacular.env in it
13. Run `python proj1.py`
14. If on cloud9 clicking Preview, then Preview Running Application, should open the site


### List of known problems
1.  Currently if spoonacular requests run out a random recipe is picked from a list common recipe names.  
    In the future I want to store the jsons returned by spoonacular and load them when requests run out.  
    The json.dump() method would be used to write the json to a file after receiving it from spoonacular.  
    When proj1.py receives a failure status from spoonacular it would load a random recipe from the json file using the json.load() method.
2.  


### List of technical issues and how they were solved
1.  CSS files were not updating after changing them. I made sure I saved everything, tried logging out of cloud9 and logging back in, and using a private window   
    (its the same thing as incognito in chrome). The fix was simply clearing the cache when reloading the page. (Ctrl+Shift+r)
2.  The twitter API would occasionally not return anything. I tried searching the recipe on the twitter page and would receive a lot of results.  
    I googled the tweepy search method at first to find any info on the method like extra parameters that might help with searching.  
    None of the additional parameters helped the issue. I then went to the twitter developer page and found the documentation for the standard serach api.  
    The standard search api only provides results for the last 7 days which is why I would occasionally get nothing. I then changed my project to pull  
    a new recipe until it received one that also had a relevant tweet. 
