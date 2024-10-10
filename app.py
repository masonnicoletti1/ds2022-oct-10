#!/usr/bin/python3

import json
import requests
import logging
import time

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)
response = json.loads(response.text)
#print(response.text)

#Assign values from json
id = response["id"]
setup = response["setup"]
punchline = response["punchline"]


#Tell joke
print("Joke ID: " + str(id))
print(setup)
time.sleep(3)
print(punchline)


#Log Joke
logger = logging.getLogger(__name__)
logging.basicConfig(filename="joke.log", encoding="utf-8", level=logging.DEBUG)
logging.warning("%s:%s:%s", id, setup, punchline)

