import requests
import json

class Generator:
    def __init__(self,nutrition_input:list,ingredients:list=[],ingredients_to_avoid_txt=[],params:dict={'n_neighbors':5,'return_distance':False}):
        self.nutrition_input=nutrition_input
        self.ingredients=ingredients
        self.ingredients_to_avoid_txt=ingredients_to_avoid_txt
        self.params=params

    def set_request(self,nutrition_input:list,ingredients:list,ingredients_to_avoid_txt:list,params:dict):
        self.nutrition_input=nutrition_input
        self.ingredients=ingredients
        self.ingredients_to_avoid_txt=ingredients_to_avoid_txt
        self.params=params

    def generate(self,):
        request={
            'nutrition_input':self.nutrition_input,
            'ingredients':self.ingredients,
            'ingredients_to_avoid_txt':self.ingredients_to_avoid_txt,
            'params':self.params
        }
        response=requests.post(url='http://3.91.201.92/predict/',data=json.dumps(request))
        return response
