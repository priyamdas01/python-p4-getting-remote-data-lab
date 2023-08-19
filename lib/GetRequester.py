import requests
import json


class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        return requests.get(self.url).content

    def load_json(self):
        json_data = json.loads(self.get_response_body())
        return json_data


print(GetRequester("http://data.cityofnewyork.us/resource/uvks-tn5n.json").load_json())
