from query_handler_base import QueryHandlerBase
import random
import requests
import json

class ChuckNorrisHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "chuck" in query:
            return True
        return False

    def process(self, query):
        try:
            result = self.call_api()
            joke = result["value"]
            self.ui.say(f"{joke}%")
        except: 
            self.ui.say("Oh no! There was an error trying to contact Chuck Norris api.")
            self.ui.say("Try something else!")



    def call_api(self):
        url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

        headers = {
            "accept": "application/json",
            "X-RapidAPI-Key": "60e8ff77bcmshea348ab246cd4e6p11b3f1jsn441dcc548ebf",
            "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)

        print(response.json())
