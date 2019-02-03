import io
import os
import json

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

class Image_Recognition:

    def __init__(self, type, num):
        self.type = type                            #type of image (from original version)
        self.LABEL = []                             #Array of Labels from Cloud-Vision-API
        self.TEXT = []                              #Array of Tests from Cloud-Vision-API
        self.num = num                              #number of items (from original)
        self.item = {                               #end Dict/JSON passd out
            "type": self.type,
            "food": self.LABEL,
            "text": self.TEXT,
            "num" : self.num
        }

    def Recognize_Image(self, imname, side = None):     #Cloud-Vision-API
        self.side = side                                #which side of text (front of consumer good vs. back)
        self.imname = imname
        # Instantiates a client
        client = vision.ImageAnnotatorClient()

        # The name of the image file to annotate
        file_name = self.imname

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        if (self.type == 'NoName') and (self.side == None):
            # Performs label detection on the image file
            response= client.label_detection(image=image)
            labels = response.label_annotations
            for label in labels:
                self.LABEL.append(label.description)

        self.export2json()                              #exports to JSON file function

        return (str(self.item['food'][1]))
        #if self.type == 'Consumer_Product':                                        #legacy code
        #    response_text = client.document_text_detection(image = image)
        #    document = response_text.full_text_annotation
        #    #respose_text = client.text_detection(image = image)
        #    #words = response_text. NEED FUNCTION
        #
        #    if self.side == 'front':
        #        # Performs label detection on the image file
        #        response= client.label_detection(image=image)
        #        labels = response.label_annotations
        #        for label in labels:
        #            self.LABEL.append(label.description) #save to a JSON file
        #    if self.side == 'back':
        #        for page in document.pages:
        #            for block in page.blocks:
        #                for paragraph in block.paragraphs:
        #                        for word in paragraph.words:
        #                            for symbol in word.symbols:
        #                                self.TEXT.append(symbol.text) #save to json file

    def export2json(self):
        with open(self.item['food'][1] +'.json', 'w') as outfile:               #publishes the export to JSON
            json.dump(self.item, outfile)
        


#Im = Image_Recognition('Consumer_Product', 1)
#Im.Recognize_Image('test_oj.jpeg', 'front')
#Im.Recognize_Image('nut_label.jpg', 'back')
#print(json.dumps(Im.item, indent = 4))

#Im = Image_Recognition('NoName', 1)
#Im.Recognize_Image('tomato.jpg')