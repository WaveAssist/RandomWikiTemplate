import waveassist
import requests

waveassist.init("2fec42dd-492b-4294-8154-d33c3ccf", "darshika_test")

response = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary")
response.raise_for_status()

wiki_data = response.json()

waveassist.store_data("wiki_summary", wiki_data)
