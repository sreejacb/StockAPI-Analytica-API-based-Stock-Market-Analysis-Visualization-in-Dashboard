import requests
import json

url = "https://latest-stock-price.p.rapidapi.com/price"

querystring = {"Indices":"NIFTY 50"}

headers = {
	"X-RapidAPI-Key": "a66b826b80msh4bb2388b0f46dddp1bd641jsn9f6a5ba0bee0",
	"X-RapidAPI-Host": "latest-stock-price.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()
with open('stock_price.json', 'w') as f:
    json.dump(data, f)