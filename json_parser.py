import json
import os

class json_parser:

    def __init__(self, json_file):
        with open(json_file, 'r') as json_file:         #opening JSON file as a dict
            data = json.load(json_file)

        print(data)
        print('\n \n \n \n \n --------------- HERE ------------------ \n \n')

        self.json_file = data               #input JSON file
        self.name = []                      #series of arrays which will be populated by the JSON from the API (get_recipe.py) 
        self.ingredients = []
        self.health = []
        self.time = []
        self.cals = []
        self.img = []
        self.link = []

        self.ingr_recipe_item = {
            "ingredient" : self.json_file['q'],                            #Dict/JSON file output 
            "recipe" : self.name,
            "For_Recipe" : self.ingredients,
            "health" : self.health,
            "time" : self.time,
            "cals" : self.cals,
            "img" : self.img,
            "link" : self.link
        }  
        

    def parser(self):
        size = len(self.json_file['hits'])              #json_file is the file with the API output
        #print(size)
        for i in range(0, size):                                                            #populating the arrays
            self.name.append(self.json_file['hits'][i]['recipe']['label'])
            self.ingredients.append(self.json_file['hits'][i]['recipe']['ingredients'])
            self.health.append(self.json_file['hits'][i]['recipe']['totalNutrients']['FAT'])
            self.time.append(self.json_file['hits'][i]['recipe']['totalTime'])
            self.cals.append(self.json_file['hits'][i]['recipe']['totalNutrients']['ENERC_KCAL']['quantity'])
            self.img.append(self.json_file['hits'][i]['recipe']['image'])
            self.link.append(self.json_file['hits'][i]['recipe']['url'])

        self.export2json()

        return self.ingr_recipe_item   #returned for main.py


    def export2json(self): 
        with open(self.json_file['q'] + '_condensed_' + '.json', 'w') as outfile:
            json.dump(self.ingr_recipe_item, outfile)

#JP = json_parser('Bush tomato_rec_.json')
#JP.parser()