import requests
api_url = "https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=boolean"

data = response =requests.get(api_url).json()

question_data = data["results"]