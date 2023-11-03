from query_handler_base import QueryHandlerBase
import random
import requests
import json

class SteamGamesHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "steam" in query:
            return True
        return False

    def process(self, query):
        params = query.split()
        start = params[1]
        count = params[2]
        region=params[3]

        try:
            result = self.call_api(start,count,region)
            games_list = result["games_list"]
            self.ui.say(f"list of games: {games_list}%")

        except: 
            self.ui.say("Oh no! There was an error trying to contact Love api.")
            self.ui.say("Try something else!")



    def call_api(self, start, count,region):
       
        url = "https://steamgames-special-offers.p.rapidapi.com/games_list/"

        querystring = {"start":start,"count":count,"region":region}

        headers = {
            "X-RapidAPI-Key": "60e8ff77bcmshea348ab246cd4e6p11b3f1jsn441dcc548ebf",
            "X-RapidAPI-Host": "steamgames-special-offers.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        print(response.json())

