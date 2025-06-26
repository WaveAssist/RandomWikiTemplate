import waveassist
import requests

waveassist.init()

response = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary")
response.raise_for_status()

wiki_data = response.json()

waveassist.store_data("wiki_summary", wiki_data)
