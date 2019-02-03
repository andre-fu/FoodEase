import requests
import json
import io
from flask import jsonify
import time

class get_recipe:

    def __init__(self, food_items):
        self.food_items = food_items #JSON entires 
        
    def poll_edamam(self):
        #publi & private API keys for Edamam
        api_id = "30186f3d"     
        api_key = "a501e2bf9eed753d4b1f792bcf592e34"

        response = requests.get("https://api.edamam.com/search?q="+ self.food_items +"&app_id=" + api_id + "&app_key=" + api_key + "&from=0&to=1&calories=591-722")
        #time.sleep(20)
        #print(response.json())
        #print('\n \n \n \n \n --------------- HERE ------------------ \n \n')
        #response = '{}'
        #info = json.loads(response)
        #data = json.dumps(response.json())
        with open(self.food_items + '_rec_.json', 'w') as outfile:  #publishing JSON file
            #print(response.json())
            json.dump(response.json(), outfile)
            #outfile.write(data)
        
        return (str(self.food_items) + '_rec_.json') #returns for main.py indexing
        
        #print ('here inside get rec')               #legacy code
        #print(self.food_items)
        #return(self.food_items + '.json')

#gr = get_recipe(food_items = 'Bush tomato')
#gr.poll_edamam()
