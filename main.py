from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
from json_parser import json_parser
from OCR import Image_Recognition
from get_recipe import get_recipe

import os
from PIL import Image
import cv2
import glob
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
#@app.route('/fileUpload.php')
#def static_from_root():
#    return send_from_directory(app.static_folder, request.path[1])

@cross_origin()
def run_flask():
    path = '/mnt/c/Users/andre/Desktop/QHacks_2019/' #personal path
    #path = '~/Desktop/QHacks/Uploads' #Keefe's directory NOT yours! 
    #path = 'the path to your image directory'
    # Store the image file names in a list as long as they are jpgs
    images = [f for f in os.listdir(path) if os.path.splitext(f)[-1] == '.jpg']  #opens and indexes images
    
    print(images)

    for image in images:
        
        Image.open(image)
    JSON_list_3 = []
    print (images)
    # if (len(images)):                                   #will only run when the files have more than 5 .jpg images
    JSON_list = []
    for j in range (0, len(images)):  
        Im = Image_Recognition('NoName', 1)
        js_needed = Im.Recognize_Image(images[j])           #step 1: recognize the content of the image
        JSON_list.append(js_needed)
    #print (JSON_list)

    JSON_list_2 = []
    for k in range (0, len(images)):                        #step 2: use API to get recipes & nutritional data
        gr = get_recipe(JSON_list[k])
        jr_gr = gr.poll_edamam()
        JSON_list_2.append(jr_gr)

    #print (JSON_list_2)

    JSON_list_3 = []
    for y in range (0, len(images)):                        #step 3: parses the API output to pass to front end 
        jp = json_parser(JSON_list_2[y])
        json_jp = jp.parser()
        JSON_list_3.append(json_jp)

    return jsonify(JSON_list_3)
        



    