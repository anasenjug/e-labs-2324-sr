from query_handler_base import QueryHandlerBase
import random
import requests
import json

class EarthQuakeHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "earthquake" in query:
            return True
        return False

    def process(self, query):
        params = query.split()
        interval = params[1]
        count=params[2]
 

        try:
            result = self.call_api(interval, count)
            print(result)
            earthquake_list = result["interval","count","radius"]
            self.ui.say(f"Earthquakes around you: {earthquake_list}%")
        except: 
            self.ui.say("Oh no! There was an error trying to contact Earthquake API.")
            self.ui.say("Try something else!")



    def call_api(self,interval,count):

        url = "https://everyearthquake.p.rapidapi.com/recentEarthquakes"

        querystring = {"interval":interval,"count":count}

        headers = {
            "X-RapidAPI-Key": "60e8ff77bcmshea348ab246cd4e6p11b3f1jsn441dcc548ebf",
            "X-RapidAPI-Host": "everyearthquake.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        print(response.json())