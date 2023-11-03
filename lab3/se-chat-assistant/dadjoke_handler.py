from query_handler_base import QueryHandlerBase
import random
import requests
import json

class DadJokeHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "dad joke" in query:
            return True
        return False

    def process(self, query): 
        try:
            result = self.call_api()
            text = result["joke"]
            self.ui.say(f"Your random dad joke is {text}%")
        except: 
            self.ui.say("Oh no! There was an error trying to contact Dad Jokes API.")
            self.ui.say("Try something else!")



    def call_api(self):
        url = "https://dad-jokes7.p.rapidapi.com/dad-jokes/joke-of-the-day"
        headers = {
            "X-RapidAPI-Key": "60e8ff77bcmshea348ab246cd4e6p11b3f1jsn441dcc548ebf",
            "X-RapidAPI-Host": "dad-jokes7.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        print(response.json())  
