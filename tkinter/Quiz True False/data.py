import requests

params = {"amount":20,"type":"boolean"}

respond = requests.get("https://opentdb.com/api.php",params=params)
respond.raise_for_status()
question_data = respond.json()["results"]