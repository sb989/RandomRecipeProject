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
8. Install flask, fuzzywuzzy and python-dotenv by using one of the commands above, and replacing tweepy with the name of the program (e.g. pip install flask)
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
    (A .gitignore is not included with the repo because I keep my keys in a seperate folder)
13. Run `python proj1.py`
14. If on cloud9 clicking Preview, then Preview Running Application, should open the site


### List of known problems
1.  If spoonacular does not provide an image with the recipe a placholder image is used. In the future  
    I would like to use pixabay, an image search api, to retrieve many photos for a recipe, so a placeholder  
    image is never needed. A request to pixabay returns a Json with urls and other information for photos.  
    
2.  The website is not responsive. This can be fixed by creating a meta tag to adjust the viewport in the html  
    and adjusting the css to not use any hardcoded values for positions, margins, widths or heights.

3.  No pagination is set up for the search results so they all show up on one page. Depending on the number of results  
    the javascript would create the appropriate amount of buttons for the pagination. This would be done using a for  
    loop, createElement and appendChild methods. The results would be stored in an array and when a button is clicked  
    it loads the appropriate results from the array.

### List of technical issues and how they were solved
1.  CSS files were not updating after changing them. I made sure I saved everything, tried logging out of cloud9 and logging back in, and using a private window   
    (its the same thing as incognito in chrome). The fix was simply clearing the cache when reloading the page. (Ctrl+Shift+r)
2.  The twitter API would occasionally not return anything. I tried searching the recipe on the twitter page and would receive a lot of results.  
    I googled the tweepy search method at first to find any info on the method like extra parameters that might help with searching.  
    None of the additional parameters helped the issue. I then went to the twitter developer page and found the documentation for the standard serach api.  
    The standard search api only provides results for the last 7 days which is why I would occasionally get nothing. I then changed my project to pull  
    a new recipe until it received one that also had a relevant tweet. 
3.  I was unsure of how to pass the results to the javascript file from the python file. The solution was to create a script in the html that created a variable  
    that took in the output from python. Then this variable was used in the javascript file.

### Future Improvements
1.  Create a collage of images that fade in and out to load new images.
2.  Create a window with a scroll bar for multiple tweets.
3.  Include descriptions of the recipe in the search results area and on the recipe page.
4.  Improve the overall look of the website (maybe use a bootstrap theme).
