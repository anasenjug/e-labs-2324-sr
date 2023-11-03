import requests

url = "https://love-calculator.p.rapidapi.com/getPercentage"

querystring = {"fname":"John","sname":"Alice"}

headers = {
	"X-RapidAPI-Key": "60e8ff77bcmshea348ab246cd4e6p11b3f1jsn441dcc548ebf",
	"X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())