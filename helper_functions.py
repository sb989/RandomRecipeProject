import json
import random
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

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

def load_random_recipe():
    file = open('recipes.json','r')
    recipes = json.load(file)
    size = recipes["nextEntry"]
    entry = random.randint(0,size-1)
    recipe = recipes["recipes"][entry]
    return recipe

def load_recipe(index):
    file = open('recipes.json','r')
    recipes = json.load(file)
    recipe = recipes["recipes"][index]
    return recipe
    
def search_results(query):
    carrot = 'static/carrot.png'
    file = open('recipes.json','r')
    recipes = json.load(file)
    size = recipes['nextEntry']
    recipe_names = []
    count = 0
    for recipe in recipes["recipes"]:
        recipe_names.append([recipe['title'],count])
        count +=1
    results = process.extract(query,recipe_names,limit = 10)
    ret = {"results":[]}
    for recipe in results:
        if recipe[1] < 80:
            continue
        index = recipe[0][1]
        info = recipes["recipes"][index]
        title = info["title"]
        id_num = info["id"]
        
        if "image" not in info:
            img = carrot
        else:
            img = info["image"]
            
        ret["results"].append({"id":id_num,"title":title,"image":img,"index":index})
        
    return ret
    
    